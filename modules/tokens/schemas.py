"""
Módulo responsável por armazenar os Schemas (modelos Pydantic) do submódulo 'token',
que serão utilizados para realizar as validações dos dados recebidos nas requisições,
antes de persisti-los na camada de armazenamento e para serializar os dados retornados
nas respostas.
"""

from typing import Dict, Optional, Union

from ninja import Schema, Field
from ninja.schema import DjangoGetter
from ninja_jwt.schema import TokenObtainPairInputSchema, SchemaInputService
from pydantic import model_validator


class UserLoginBase(Schema):
    full_name: Optional[str] = Field(None, description='Nome completo')
    email: Optional[str] = Field(None, description='Email')
    username: Optional[str] = Field(None, description='Username')
    is_admin: Optional[bool] = Field(None, description='Administrador')

    @staticmethod
    def from_user(user):
        return UserLoginBase(
            full_name=user.username,
            email=user.email,
            username=user.username,
            is_admin=user.is_admin,
        )


class CustomTokenObtainOutSchema(Schema):
    token: str = Field(..., description='Token de acesso')
    user: UserLoginBase = Field(..., description='Usuário')


class CustomTokenObtainSchema(TokenObtainPairInputSchema):
    """
    Schema responsável por tratar o Schema (modelo Pydantic) de entrada para o login.
    """

    @model_validator(mode='before')
    def validate_inputs(
        cls, values: Union[DjangoGetter, Dict]
    ) -> Dict:
        schema_input = SchemaInputService(values, cls.model_config)
        input_values = schema_input.get_values()
        request = schema_input.get_request()

        if isinstance(input_values, dict):
            values.update(cls.validate_values(request=request, values=input_values))
        return values

    def output_schema(self) -> CustomTokenObtainOutSchema:
        token = self.to_response_schema().access
        user_schema = UserLoginBase.from_user(self._user)
        return CustomTokenObtainOutSchema(token=token, user=user_schema)
