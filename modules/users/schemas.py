from datetime import datetime
from typing import List, Optional
from ninja import Field, FilterSchema, ModelSchema, Schema

from .models import CustomUser

class GetBaseSchema(Schema):
    """
    Schema responsável por mostrar o id de saída para os dados genéricos.
    """

    id: int = Field(..., description="ID")


class UserFilter(FilterSchema):  
    """
    Schema responsável por armazenar o Schema (modelo Pydantic) de filtro para os usuários.
    """

    username_id: int = Field(None, q='id__exact', description='ID do usuário')
    username: str = Field(
        None, q='username__istartswith', description='Nome de usuário'
    )
    is_active: bool = Field(None, q='is_active', description='Está ativo?')


class UserInPost(ModelSchema):
    """
    Schema responsável por armazenar o Schema (modelo Pydantic) de entrada para os usuários.
        - username: Nome de usuário;
        - password: Senha;
    """

    class Meta:  # pylint: disable=missing-class-docstring
        model = CustomUser
        fields = [
            'username',
            'password',
        ]


class UserInPut(ModelSchema):
    """
    Schema responsável por alterar os dados dos usuários.
        - username: Nome de usuário;
        - password: Senha;
        - is_active: Está ativo?
    """

    class Meta:  # pylint: disable=missing-class-docstring
        model = CustomUser
        fields = [
            'password',
        ]


class UserList(Schema):
    """
    Schema responsável por listar os dados dos usuários.
    """

    id: int = Field(..., description='ID do usuário')
    username: str = Field(..., description='Nome de usuário')
    is_active: bool = Field(..., description='Está ativo?')


class UserNameOut(Schema):
    """
    Schema responsável por visualizar o nome do usuário.
    """

    id: int = Field(..., description='ID do usuário')
    username: str = Field(..., description='Nome de usuário')

class UserOut(Schema):
    """
    Schema responsável por visualizar a saída dos dados de usuário.
    """
    id: int
    username: str
    email: str
    profile_picture: Optional[str] = None
    date_joined: datetime
    is_active: bool


class UserPostSchema(Schema):
    username: str
    email: str
    password: str
    favorite_sports: List[int]
    phone_number: str