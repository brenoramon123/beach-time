from typing import Any, Dict, Optional, Tuple, Union

from django.db import models, transaction
from django.db.utils import IntegrityError
from django.http import Http404
from ninja_extra import status

from core.utils.classes import Service

from ninja import UploadedFile, File

from core.utils.validators import normalize_phone
from modules.users.repository import UserRepository



class UserService(Service):
    """
    """

    repository = UserRepository
    
    @classmethod
    def validate_payload(
        cls, *, payload: Dict[str, Any], id: Optional[int] = None, **kwargs
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        instance: Optional[models.Model] = None
        
        favorite_sports = kwargs.get('sports_list') or []
        phone_number = payload.get('phone_number', '').strip()
        
        phone_number_normalized = normalize_phone(phone_number)
        
        print(phone_number_normalized)
        
        for sport in favorite_sports:
            status_code, sport = cls.SportsService.get(id=sport)
            if status_code != status.HTTP_200_OK:
                return status_code, sport
        if id:
            status_code, instance = cls.get(id=id)
            
            if status_code != status.HTTP_200_OK:
                return status_code, instance
            
            if not instance.is_active:
                return status.HTTP_400_BAD_REQUEST, {
                    'message': 'O usuário foi desativado.'
                }
        else:
            
            pass

        return status.HTTP_200_OK, instance

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
                cls.validate_payload(payload=payload)
                
                favorite_sports = payload.pop('favorite_sports', [])
                
                instance = cls.repository.post(payload=payload, file=file)
                
                for sport in favorite_sports:
                    status_code, sport = cls.SportsService.get(id=sport)
                    if status_code != status.HTTP_200_OK:
                        return status_code, sport
                    instance.favorite_sports.add(sport)
                return status.HTTP_201_CREATED, instance
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
