from typing import Any, Dict, Optional, Tuple
from ninja_extra import status

from django.db import models
from core.utils.classes import Service
from modules.sports.repository import SportsRepository



class SportsService(Service):
    """

    """

    repository = SportsRepository

    @classmethod
    def validate_payload(
        cls, *, payload: Dict[str, Any], id: Optional[int] = None, **kwargs
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        """

        """
        status_code: int
        django_admin: bool = kwargs.get('django_admin', False)
        name = payload.get('name', '').strip()
        instance: Optional[models.Model] = None
        if id is None:
            pass
            if not name:
                return status.HTTP_400_BAD_REQUEST, {'name': 'O nome do esporte é obrigatório.'}
        else:
            pass

        return status.HTTP_200_OK, instance

