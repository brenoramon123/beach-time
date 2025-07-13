from typing import Dict

from django.db import models
from django.http import Http404

from core.utils.classes import Repository
from core.utils.filters_characters import remove_excess_spaces

from .models import City, Country, FederativeUnit


class CountryRepository(Repository):
    """
    Responsável por lidar com a persistência e interação
    com a camada de armazenamento de dados, relacionados ao submódulo de pais.
    """

    model = Country

    # Country
    @classmethod
    def update_payload(
        cls, *, payload: Dict, last_user_id: int, **kwargs
    ) -> Dict:
        """
        Método responsável por atualizar o payload do país.
        """
        updated_payload: Dict = super().update_payload(
            payload=payload, last_user_id=last_user_id
        )
        updated_payload.update({
            'name': remove_excess_spaces(
                updated_payload.get('name', '')
            ).upper(),
            'abbreviation': remove_excess_spaces(updated_payload.get('abbreviation', '').upper()),
        })
        return updated_payload


class FederativeUnitRepository(Repository):
    """
    Responsável por lidar com a persistência e interação
    com a camada de armazenamento de dados, relacionados ao submódulo de unidade federativa.
    """

    model = FederativeUnit

    @classmethod
    def update_payload(
        cls, *, payload: Dict, last_user_id: int, **kwargs
    ) -> Dict:
        """
        Método responsável por atualizar o payload da unidade federativa.
        """
        updated_payload: Dict = super().update_payload(
            payload=payload, last_user_id=last_user_id
        )
        updated_payload.update({
            'name': remove_excess_spaces(
                updated_payload.get('name', '')
            ).upper(),
            'abbreviation': remove_excess_spaces(updated_payload.get('abbreviation', '').upper()),
        })
        return updated_payload


class CityRepository(Repository):
    """
    Responsável por lidar com a persistência e interação
    com a camada de armazenamento de dados, relacionados ao submódulo de cidade.
    """

    model = City

    @classmethod
    def update_payload(
        cls, *, payload: Dict, last_user_id: int, **kwargs
    ) -> Dict:
        """
        Método responsável por atualizar o payload da cidade.
        """
        updated_payload: Dict = super().update_payload(
            payload=payload, last_user_id=last_user_id
        )
        updated_payload.update({
            'name': remove_excess_spaces(
                updated_payload.get('name', '')
            ).upper(),
        })
        return updated_payload

