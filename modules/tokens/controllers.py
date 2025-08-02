from ninja_extra import api_controller, route
from ninja_jwt.controller import ControllerBase

from core.utils.constants import MASK_USER_ENUMERATION, OTP_MAX_ATTEMPTS, OTP_TTL_SECONDS, RESEND_COOLDOWN, TEMP_TOKEN_TTL
from core.utils.validators import generate_otp, normalize_phone, otp_cache_keys, send_sms
from modules.users.services import UserService

from .schemas import CodeVerificationSchema, CustomTokenObtainOutSchema, CustomTokenObtainSchema, PhoneSchema
from django.core.cache import cache
import secrets
from ninja_extra import status


@api_controller('core/', tags=['CORE - TOKENS'], auth=None)
class TokenJWTController(
    ControllerBase,
):
    """
    Responsável por autenticar o token da requisição, retornando informações
    para o front-end sobre as permissões do usuário.
    """

    @route.post(
        'token', response=CustomTokenObtainOutSchema, url_name='token_obtain'
    )
    def obtain_token(self, request, user_token: CustomTokenObtainSchema):
        """
        Rota responsável por autenticar o token da requisição, retornando informações
        para o front-end sobre as permissões do usuário.
        ------------------------------------------------------------------------------
        """
        user_token.check_user_authentication_rule()
        return user_token.output_schema()


    @route.post("/auth/request-code")
    def request_code(self, request, payload: PhoneSchema):
        try:
            phone = normalize_phone(payload.phone)
        except ValueError as e:
            return status.HTTP_400_BAD_REQUEST, {"message": str(e)}

        k = otp_cache_keys(phone)

        if cache.get(k["resend"]):
            return status.HTTP_429_TOO_MANY_REQUESTS, {"message": "Aguarde um instante para solicitar novo código."}

        user = UserService.list().filter(phone_number=phone).exists()
    
        if not user and not MASK_USER_ENUMERATION:
            return 404, {"message": "Usuário não encontrado."}

        otp = generate_otp()
        cache.set(k["otp"], otp, OTP_TTL_SECONDS)
        cache.set(k["attempts"], 0, OTP_TTL_SECONDS)
        cache.set(k["resend"], 1, RESEND_COOLDOWN)

        send_sms(phone, f"Seu código de login é: {otp}. Ele expira em 5 minutos.")

        if MASK_USER_ENUMERATION:
            return {"message": "Se o número existir, enviaremos um código por SMS."}
        return {"message": "Código enviado por SMS."}


    @route.post("/auth/verify-code")
    def verify_code(self, request, payload: CodeVerificationSchema):
        try:
            phone = normalize_phone(payload.phone)
        except ValueError as e:
            return status.HTTP_400_BAD_REQUEST, {"message": str(e)}

        k = otp_cache_keys(phone)
        otp = cache.get(k["otp"])
        if not otp:
            return status.HTTP_401_UNAUTHORIZED, {"message": "Código inválido ou expirado."}

        attempts = cache.get(k["attempts"]) or 0
        if attempts >= OTP_MAX_ATTEMPTS:
            cache.delete_many([k["otp"], k["attempts"]])
            return status.HTTP_423_LOCKED, {"message": "Muitas tentativas. Solicite um novo código."}

        if payload.code != otp:
            cache.incr(k["attempts"])
            return status.HTTP_401_UNAUTHORIZED, {"message": "Código inválido."}

        cache.delete_many([k["otp"], k["attempts"]])
        temp_token = secrets.token_urlsafe(32)
        cache.set(k["temp"], temp_token, TEMP_TOKEN_TTL)

        return {"message": "Código validado.", "temp_token": temp_token}

    @route.post("/auth/login", response=CustomTokenObtainOutSchema)
    def final_login(self, request, user_token: CustomTokenObtainSchema):
        try:
            phone = normalize_phone(user_token.phone)
        except ValueError as e:
            return status.HTTP_400_BAD_REQUEST, {"message": str(e)}

        k = otp_cache_keys(phone)
        stored_temp = cache.get(k["temp"])
        if not stored_temp or stored_temp != user_token.temp_token:
            return status.HTTP_400_BAD_REQUEST, {"message": "Credenciais inválidas."}

        user = UserService.list().filter(phone_number=phone).first()
        if not user:
            if MASK_USER_ENUMERATION:
                return status.HTTP_401_UNAUTHORIZED, {"message": "Credenciais inválidas."}
            return status.HTTP_404_NOT_FOUND, {"message": "Usuário não encontrado."}

        if not user.check_password(user_token.password):
            return status.HTTP_401_UNAUTHORIZED, {"message": "Credenciais inválidas."}

        cache.delete(k["temp"])

        user_token.check_user_authentication_rule()
        return user_token.output_schema()
