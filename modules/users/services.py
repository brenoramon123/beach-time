from typing import Any, Dict, Optional, Tuple, Union

from django.db import models, transaction
from django.db.utils import IntegrityError
from django.http import Http404
from ninja_extra import status

from core.utils.classes import Service

from ninja import UploadedFile, File

from modules.users.repository import UserRepository



class UserService(Service):
    """
    """

    repository = UserRepository


    @classmethod
    def get(cls, *, id: int) -> Tuple[int, models.Model | Dict[str, str]]:  
        instance_model: models.Model = (
            cls.repository.model._meta.verbose_name.capitalize()
        )
        try:
            instance = cls.repository.get(id=id)
            if instance.is_admin:
                return status.HTTP_404_NOT_FOUND, {
                    'message': f'{instance_model} não existe.'
                }
            return status.HTTP_200_OK, instance
        except Http404:
            return status.HTTP_404_NOT_FOUND, {
                'message': f'{instance_model} não existe.'
            }

    @classmethod
    def post(
        cls, *, payload: Dict[str, Any], file: Optional[UploadedFile] = File(None), **kwargs
    ) -> Tuple [int, Union[models.Model, Dict[str, str]]]:
        try:
            with transaction.atomic():
                instance = cls.repository.post(payload=payload, file=file)
                return status.HTTP_201_CREATED, instance
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
