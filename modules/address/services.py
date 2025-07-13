from typing import Any, Dict, List, Optional, Tuple

from django.db import IntegrityError, models
from ninja_extra import status
from django.db import models, transaction

from core.utils.classes import Service
from core.utils.filters_characters import  remove_excess_spaces

from .repository import (
    CityRepository,
    CountryRepository,
    FederativeUnitRepository,
)


class CountryServices(Service):
    """
    Responsável por implementar os serviços relacionados ao submódulo de pais,
    utilizados para realizar operações sobre regras de negócio, antes de persistir
    os dados na camada de armazenamento.
    As regras de negócio implementadas são:
        - Não permitir que o nome do país seja vazio;
        - Não permitir que a sigla do país seja vazia;
        - Não permitir que a sigla do país tenha menos de três caracteres
          e permitir apenas letras;
        - Não permitir que o nome do país seja duplicado;
        - Não permitir que a sigla do país seja duplicada;
        - Não permitir que o país seja inativado, caso exista alguma unidade federativa vinculada;
        - Não permitir alterar o país inativo;
    """

    repository = CountryRepository

    @classmethod
    def validate_payload(
        cls,
        *,
        payload: Dict[str, Any],
        id: Optional[int] = None,
        **kwargs,  
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        """
        Método responsável por implementar as regras de negócio do submódulo de país.
        """
        status_code: int
        message: Dict
        country: Optional[models.Model] = None
        django_admin: Optional[bool] = kwargs.get('django_admin', False)

        get_name: str = remove_excess_spaces(payload.get('name', '')).upper()
        if get_name == '':
            return status.HTTP_400_BAD_REQUEST, {
                'message': 'Nome do país não pode ser vazio.'
            }

        get_abbreviation: str = remove_excess_spaces(
            payload.get('abbreviation', '')
        ).upper()
        if get_abbreviation == '':
            return status.HTTP_400_BAD_REQUEST, {
                'message': 'Sigla do país não pode ser vazia.'
            }

        if (
            len(get_abbreviation.strip()) != 3
            or not get_abbreviation.isalpha()
        ):
            return status.HTTP_400_BAD_REQUEST, {
                'message': 'Sigla deve possuir exatamente três letras.'
            }

        country_list = cls.list()
        country_filter_name = country_list.filter(
            name=get_name, is_active=True
        )
        country_filter_abbreviation = country_list.filter(
            abbreviation=get_abbreviation, is_active=True
        )
        if id is not None:
            status_code, country_or_message = cls.get(id=id)
            if status_code != status.HTTP_200_OK:
                message = country_or_message
                return status_code, message

            country: Any = country_or_message

            if not country.is_active and not django_admin:
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'País inativo, não é possível modificar suas informações.'
                }

            if country_filter_name.exclude(id=id).exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe este país.'
                }

            if country_filter_abbreviation.exclude(id=id).exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe esta sigla.'
                }

        else:
            if country_filter_name.exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe este país.'
                }

            if country_filter_abbreviation.exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe esta sigla.'
                }

        return status.HTTP_200_OK, country
    
    @classmethod
    def multiples(cls, payload: List[Dict[str, Any]], last_user_id: int) -> Tuple[int, List[models.Model] | List[Dict[str, str]]]:
        try:
            with transaction.atomic():
                countries_created = []
                print("payload no controller:", payload)
                for item in payload:
                    status_code, message_or_object = cls.post(payload=item, last_user_id=last_user_id)
                    if status_code != status.HTTP_201_CREATED:
                        print("status code:", status_code)
                        return status_code, message_or_object
                    countries_created.append(message_or_object)

                print("responsee:", countries_created)
                return status.HTTP_201_CREATED, countries_created
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, [{
                'message': str(error)
            }]



class FederativeUnitServices(Service):
    """
    Responsável por implementar os serviços relacionados ao submódulo de unidade federativa,
    utilizados para realizar operações sobre regras de negócio, antes de persistir
    os dados na camada de armazenamento.
    As regras de negócio implementadas são:
        - Não permitir que o nome da unidade federativa seja vazio;
        - Não permitir que a sigla da unidade federativa seja vazia;
        - Não permitir que a sigla da unidade federativa tenha menos de duas letras
          e permitir apenas letras;
        - Não permitir que o nome da unidade federativa seja duplicado ao país informado;
        - Não permitir que a sigla da unidade federativa seja duplicada ao país informado;
        - Não permitir que a unidade federativa seja inativada, caso exista alguma cidade vinculada;
        - Não permitir alterar o país da unidade federativa;
        - Não permitir alterar a unidade federativa inativa;
    """

    repository = FederativeUnitRepository

    @classmethod
    def validate_payload(
        cls,
        *,
        payload: Dict[str, Any],
        id: Optional[int] = None,
        **kwargs,  
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        """
        Método responsável por implementar as regras de negócio do submódulo de unidade federativa.
        """
        status_code: int
        message: Dict
        federative_unit: Optional[models.Model] = None
        django_admin: Optional[bool] = kwargs.get('django_admin', False)

        get_name: str = remove_excess_spaces(payload.get('name', '')).upper()
        if get_name == '':
            return status.HTTP_400_BAD_REQUEST, {
                'message': 'Nome da unidade federativa não pode ser vazio.'
            }

        get_abbreviation: str = remove_excess_spaces(
            payload.get('abbreviation', '')
        ).upper()
        if get_abbreviation == '':
            return status.HTTP_400_BAD_REQUEST, {
                'message': 'Sigla da unidade federativa não pode ser vazia.'
            }

        if (
            len(get_abbreviation.strip()) != 2
            or not get_abbreviation.isalpha()
        ):
            return status.HTTP_400_BAD_REQUEST, {
                'message': 'Sigla deve possuir exatamente duas letras.'
            }

        status_code, country_or_message = CountryServices.get(
            id=payload.get('country_id', None)
        )
        if status_code != status.HTTP_200_OK:
            message = country_or_message
            return status_code, message

        country: Any = country_or_message

        federative_unit_name = country.federativeunit_country_country.filter(
            name=get_name,
            is_active=True,
        )
        federative_unit_abbreviation = (
            country.federativeunit_country_country.filter(
                abbreviation=get_abbreviation,
                is_active=True,
            )
        )
        if id is not None:
            status_code, federative_unit_or_message = cls.get(id=id)
            if status_code != status.HTTP_200_OK:
                message = federative_unit_or_message
                return status_code, message

            federative_unit: Any = federative_unit_or_message

            if not federative_unit.is_active and not django_admin:
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Unidade federativa inativa, não é possível modificar suas informações.'
                }

            if payload.get('country_id') != federative_unit.country_id:
                if not country.is_active:
                    return status.HTTP_400_BAD_REQUEST, {
                        'message': 'País não está disponível.'
                    }

            if federative_unit_name.exclude(id=id).exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe esta unidade federativa neste país com este nome.'
                }

            if federative_unit_abbreviation.exclude(id=id).exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe esta sigla da unidade federativa neste país.'
                }
        else:
            if not country.is_active:
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'País não está disponível.'
                }

            if federative_unit_name.exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe esta unidade federativa neste país'
                }

            if federative_unit_abbreviation.exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe esta sigla da unidade federativa neste país.'
                }

        return status.HTTP_200_OK, federative_unit


class CityServices(Service):
    """
    Responsável por implementar os serviços relacionados ao submódulo de cidade,
    utilizados para realizar operações sobre regras de negócio, antes de persistir
    os dados na camada de armazenamento.
    As regras de negócio implementadas são:
        - Não permitir que o nome da cidade seja vazio;
        - Não permitir que a cidade seja inativada, caso exista algum bairro vinculado;
        - Não permitir que o nome da cidade seja duplicado na unidade federativa informada;
        - Não permitir alterar a unidade federativa da cidade;
        - Não permitir alterar a cidade inativa;
    """

    repository = CityRepository

    @classmethod
    def validate_payload(
        cls,
        *,
        payload: Dict[str, Any],
        id: Optional[int] = None,
        **kwargs,  
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        """
        Método responsável por implementar as regras de negócio do submódulo de cidade.
        """
        message: int
        status_code: Dict
        city: Optional[models.Model] = None
        django_admin: bool = kwargs.get('django_admin', False)

        get_name: str = remove_excess_spaces(payload.get('name', '')).upper()
        if get_name == '':
            return status.HTTP_400_BAD_REQUEST, {
                'message': 'Nome da cidade não pode ser vazio.'
            }

        status_code, federative_unit_or_message = FederativeUnitServices.get(
            id=payload.get('federative_unit_id', None)
        )
        if status_code != status.HTTP_200_OK:
            message = federative_unit_or_message
            return status_code, message

        federative_unit: Any = federative_unit_or_message

        city_name = federative_unit.city_federativeunit_federativeunit.filter(
            name=get_name,
        )
        if id is not None:
            status_code, city_or_message = cls.get(id=id)
            if status_code != status.HTTP_200_OK:
                message = city_or_message
                return status_code, message

            city: Any = city_or_message

            if not city.is_active and not django_admin:
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Cidade inativa, não é possível modificar suas informações.'
                }

            if (
                payload.get('federative_unit_id', None)
                != city.federative_unit_id
            ):
                if not federative_unit.is_active:
                    return status.HTTP_400_BAD_REQUEST, {
                        'message': 'Unidade Federativa não está disponível.'
                    }

            if city_name.exclude(id=id).exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe cidade cadastrada nesta unidade federativa com este nome.'
                }

        else:
            if not federative_unit.is_active:
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Unidade Federativa não está disponível.'
                }

            if city_name.exists():
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'Já existe cidade cadastrada nesta unidade federativa com este nome.'
                }

        return status.HTTP_200_OK, city
