"""
Módulo responsável por armazenar os Schemas (modelos Pydantic) do submódulo de endereços, que
serão utilizados para realizar as validações dos dados recebidos nas requisições, antes de
persisti-los na camada de armazenamento e para serializar os dados retornados nas respostas.
"""


from ninja import Field, FilterSchema, ModelSchema, Schema


from core.schemas import GetIdName

from .models import City, Country, FederativeUnit


# COUNTRY
class CountryFilter(FilterSchema):
    """
    Schema responsável por mostrar campos de filtragem de países.
    """

    country_id: int = Field(None, q="id__exact", description="ID do país")
    name: str = Field(None, q="name__istartswith", description="Nome do país")
    is_active: bool = Field(None, q="is_active", description="Está ativo?")


class CountryInPost(ModelSchema):
    """
    Schema responsável por armazenar os campos de entrada de países.
        - name: Nome do país;
        - abbreviation: Abreviação do país;
    """

    class Meta:  # pylint: disable=missing-class-docstring
        model = Country
        fields = [
            "name",
            "abbreviation",
        ]


class CountryInPut(ModelSchema):
    """
    Schema responsável por armazenar os campos de atualização de países.
        - name: Nome do país
        - abbreviation: Abreviação do país;
    """

    class Meta:  # pylint: disable=missing-class-docstring
        model = Country
        fields = [
            "name",
            "abbreviation",
        ]


class CountryList(Schema):
    """
    Schema responsável por listar os campos de países.
    """

    id: int = Field(..., description="ID do país")
    name: str = Field(..., description="Nome do país")
    abbreviation: str = Field(..., description="Abreviação do país")
    is_active: bool = Field(..., description="Está ativo?")


class CountryOut(ModelSchema):
    """
    Schema responsável por mostrar os campos de saída de países.
        - id: ID do país;
        - name: Nome do país;
        - abbreviation: Abreviação do país;
        - is_active: Está ativo?
    """

    class Meta:  # pylint: disable=missing-class-docstring
        model = Country
        exclude = [
            "last_user",
            "registration",
            "last_modification",
        ]


# FEDERATIVE UNIT
class FederativeUnitFilter(FilterSchema):
    """
    Schema responsável por mostrar os campos de filtragem de unidades federativas.
    """

    federative_id: int = Field(None, q="id__exact", description="ID da unidade federativa")
    name: str = Field(None, q="name__istartswith", description="Nome da unidade federativa")
    country_id: int = Field(None, q="country_id__exact", description="ID do país")
    country_name: str = Field(None, q="country__name__istartswith", description="Nome do país")
    is_active: bool = Field(None, q="is_active", description="Está ativo?")


class FederativeUnitInPost(ModelSchema):
    """
    Schema responsável por armazenar os campos de entrada de unidades federativas.
        - name: Nome da unidade federativa;
        - abbreviation: Abreviação da unidade federativa;
    """

    country_id: int = Field(..., description="ID do país")

    class Meta:  # pylint: disable=missing-class-docstring
        model = FederativeUnit
        fields = [
            "name",
            "abbreviation",
        ]


class FederativeUnitInPut(ModelSchema):
    """
    Schema responsável por armazenar os campos de atualização de unidades federativas.
        - name: Nome da unidade federativa;
        - abbreviation: Abreviação da unidade federativa;
    """

    country_id: int = Field(..., description="ID do país")

    class Meta:  # pylint: disable=missing-class-docstring
        model = FederativeUnit
        fields = [
            "name",
            "abbreviation",
        ]


class FederativeUnitList(Schema):
    """
    Schema responsável por listar os campos de unidades federativas.
    """

    id: int = Field(..., description="ID da unidade federativa")
    name: str = Field(..., description="Nome da unidade federativa")
    abbreviation: str = Field(..., description="Abreviação da unidade federativa")
    country_name: str = Field(..., alias="country.name", description="Nome do país")
    is_active: bool = Field(..., description="Está ativo?")


class FederativeUnitOut(ModelSchema):
    """
    Schema responsável por mostrar os campos de saída de unidades federativas.
        - id: ID da unidade federativa;
        - name: Nome da unidade federativa;
        - abbreviation: Abreviação da unidade federativa;
        - is_active: Está ativo?
    """

    country: GetIdName = Field(..., description="País")

    class Meta:  # pylint: disable=missing-class-docstring
        model = FederativeUnit
        exclude = [
            "country",
            "last_user",
            "registration",
            "last_modification",
        ]


# CITY
class CityFilter(FilterSchema):
    """
    Schema responsável por mostrar os campos de filtragem de cidades.
    """

    city_id: int = Field(None, q="id__exact", description="ID da cidade")
    name: str = Field(None, q="name__istartswith", description="Nome da cidade")
    federative_unit_id: int = Field(
        None,
        q="federative_unit_id__exact",
        description="ID da unidade federativa",
    )
    federative_unit_name: str = Field(
        None,
        q="federative_unit__name__istartswith",
        description="Nome da unidade federativa",
    )
    is_active: bool = Field(None, q="is_active", description="Está ativo?")


class GetCityNameFederativeUnitName(GetIdName):
    ...
    federative_unit: GetIdName = Field(
        ...,
        description="Unidade Federativa"
    )


class CityInPost(ModelSchema):
    """
    Schema responsável por armazenar os campos de entrada de cidades.
        - name: Nome da cidade;
    """

    federative_unit_id: int = Field(..., description="ID da unidade federativa")

    class Meta:  # pylint: disable=missing-class-docstring
        model = City
        fields = [
            "name",
        ]


class CityInPut(ModelSchema):
    """
    Schema responsável por armazenar os campos de atualização de cidades.
        - name: Nome da cidade;
    """

    federative_unit_id: int = Field(..., description="ID da unidade federativa")

    class Meta:  # pylint: disable=missing-class-docstring
        model = City
        fields = [
            "name",
        ]


class CityList(Schema):
    """
    Schema responsável por listar os campos de cidades.
    """

    id: int = Field(..., description="ID da cidade")
    name: str = Field(..., description="Nome da cidade")
    federative_unit_name: str = Field(
        ...,
        alias="federative_unit.name",
        description="Nome da unidade federativa",
    )
    is_active: bool = Field(..., description="Está ativo?")


class CityOut(ModelSchema):
    """
    Schema responsável por mostrar os campos de saída de cidades.
        - id: ID da cidade;
        - name: Nome da cidade;
        - is_active: Está ativo?
    """

    federative_unit: GetIdName = Field(..., description="Unidade federativa")

    class Meta:  # pylint: disable=missing-class-docstring
        model = City
        exclude = [
            "federative_unit",
            "last_user",
            "registration",
            "last_modification",
        ]
