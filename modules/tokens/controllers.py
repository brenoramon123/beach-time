from ninja_extra import api_controller, route
from ninja_jwt.controller import ControllerBase

from .schemas import CustomTokenObtainOutSchema, CustomTokenObtainSchema


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
