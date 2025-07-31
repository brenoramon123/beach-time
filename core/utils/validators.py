import re

from core.utils.constants import DEFAULT_REGION, OTP_DIGITS
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
import secrets
from ninja_extra import status

def validate_email(email: str) -> bool:
    """
    Valida emails. Retorna True ou False.
    """

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        return True
    else:
        return False

def normalize_phone(raw: str, default_region: str = DEFAULT_REGION) -> str:
    """
    Normaliza o telefone para E.164. Ex.: +55999887766
    """
    try:
        parsed = phonenumbers.parse(raw, default_region)
        if not phonenumbers.is_possible_number(parsed) or not phonenumbers.is_valid_number(parsed):
            return status.HTTP_400_BAD_REQUEST, {"message": "Telefone inválido"}

        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    except NumberParseException:
        return status.HTTP_400_BAD_REQUEST, {"message": "Telefone inválido"}

def otp_cache_keys(e164: str):
    return {
        "otp": f"otp:{e164}",
        "attempts": f"otp_attempts:{e164}",
        "resend": f"otp_resend_lock:{e164}",
        "temp": f"temp_token:{e164}",
    }

def generate_otp(digits: int = OTP_DIGITS) -> str:
    floor = 10**(digits - 1)
    span = 9 * floor
    return str(secrets.randbelow(span) + floor)

def send_sms(phone_e164: str, message: str) -> None:
    """
    Implemente com seu provedor (Twilio/AWS SNS/etc).
    Aqui deixo um stub de desenvolvimento.
    """
    print(f"[DEV SMS] para {phone_e164}: {message}")

def generate_access_token(user) -> str:
    """
    Troque por sua emissão real de JWT (e.g., SimpleJWT).
    """
    return secrets.token_urlsafe(48)
