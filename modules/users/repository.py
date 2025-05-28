"""
The Repository is responsible for dealing with how to access the data.
It encapsulates the logic of persistence and interaction with a layer of data storage,
such as a data bank or a file system.
"""

import os
from typing import Dict, Optional

from django.db import models
from django.http import Http404
from ninja import File, UploadedFile

from django.conf import settings
from core.utils.classes import Repository
from core.utils.filters_characters import remove_excess_spaces
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .models import CustomUser as User


class UserRepository(Repository):
    """
    Responsável por lidar com a persistência e interação com
    a camada de armazenamento de dados, com relação aos usuários.
    """

    model = User

    @classmethod
    def update_payload(cls, *, payload: Dict, **kwargs) -> Dict:  
        """
        Método responsável por atualizar o payload do usuário de acordo com o tipo de requisição.
        """
        instance = kwargs.get('instance', None)
        if instance is None:
            payload.update({
                'username': remove_excess_spaces(
                    payload.get('username')
                ).lower(),
            })
        return payload

    @classmethod
    def list(cls) -> models.QuerySet:
        """
        Lista todos os registros.
        """
        return cls.model.objects.exclude(is_admin=True)

    @classmethod
    def post(cls, *, payload: Dict, file: Optional[UploadedFile] = None, **kwargs) -> models.Model:
        if file:
            file_path = os.path.join('profile_pictures', file.name)
            full_path = os.path.join(settings.MEDIA_ROOT, file_path)

            # Garante que o diretório existe
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            # Salva usando o storage padrão
            default_storage.save(file_path, ContentFile(file.read()))

            payload["profile_picture"] = file_path

        password = payload.pop('password', None)
        user = cls.model(**payload)

        if password:
            user.set_password(password)

        user.save()
        return user


    @classmethod
    def put(
        cls, *, instance: models.Model, payload: Dict, **kwargs
    ) -> models.Model:
        """
        Método responsável por atualizar um usuário.
        """
        if not isinstance(instance, cls.model):
            raise Http404(
                "The instance does not belong to the model."
                f"{cls.model._meta.verbose_name}."
            )

        payload = cls.update_payload(payload=payload, instance=instance)

        for key, value in payload.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def change_password(
        cls, instance: models.Model, password: str
    ) -> models.Model:
        """
        Método responsável por atualizar um usuário.
        """
        if not isinstance(instance, cls.model):
            raise Http404(
                "The instance does not belong to the model."
                f"{cls.model._meta.verbose_name}."
            )

        instance.set_password(password)
        instance.save()

        return instance
