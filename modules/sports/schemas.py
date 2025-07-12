from typing import Optional
from ninja import Field, FilterSchema, ModelSchema, Schema
from modules.sports.models import Sports



class SportsFilter(FilterSchema):
    """
    Schema responsável por filtrar os dados dos esportes.
    """
    id: Optional[int] = Field(None, description='ID do esporte')
    name: Optional[str] = Field(None, description='Nome do esporte')
    
class SportsInPost(ModelSchema):
    """
    Schema responsável por criar os dados dos esportes.
    """
    
    class Meta:  # pylint: disable=missing-class-docstring
        model = Sports
        fields = ['name']


class SportsInPut(ModelSchema):
    """
    Schema responsável por atualizar os dados dos esportes.
    """
    
    class Meta:  # pylint: disable=missing-class-docstring
        model = Sports
        fields = ['name']

class SportsList(Schema):
    """
    Schema responsável por listar os dados dos esportes.
    """

    id: int = Field(..., description='ID do esporte')
    name: str = Field(..., description='Nome do esporte')
    
class SportsOut(ModelSchema):
    """
    Schema responsável por visualizar a saída dos dados dos esportes.
    """
    
    class Meta:  # pylint: disable=missing-class-docstring
        model = Sports
        fields = ['id', 'name', 'description', 'last_user']
        model_fields = '__all__'