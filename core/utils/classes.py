from typing import Any, Dict, List, Optional, Tuple, Union

from django.core.exceptions import FieldError
from django.db import models, transaction
from django.db.utils import IntegrityError
from django.utils.translation import gettext_lazy as _
from django.http import Http404
from django.shortcuts import get_object_or_404
from ninja_extra import status

from core.utils import omitted_fields
from core.utils.model_utils import get_active_references



class Repository:
    """
    Responsável por lidar com a persistência e interação com a camada de 
    armazenamento de dados.
    """

    model: models.Model

    @classmethod
    def update_payload(
        cls, *, payload: Dict, last_user_id: int, **kwargs
    ) -> Dict:
        updated_payload: Dict = {
            **payload,
            'last_user_id': last_user_id,
        }
        return updated_payload

    @classmethod
    def list(cls) -> models.QuerySet:
        """
        """
        return cls.model.objects.all().defer(*omitted_fields)

    @classmethod
    def get(cls, *, id: int, only: Optional[List[str]] = None) -> models.Model:
        """
        """

        if only:
            valid_fields = {field.name for field in cls.model._meta.get_fields()}
            invalid_fields = set(only) - valid_fields
            if invalid_fields:
                message: str = _("Invalid fields")
                raise FieldError(f"{message}: {', '.join(invalid_fields)}")
        queryset: models.QuerySet = cls.model.objects.only(*only) if only else cls.model.objects.all()
        return get_object_or_404(queryset, id=id)

    @classmethod
    def post(
        cls, *, payload: Dict, last_user_id: int, **kwargs
    ) -> models.Model:
        """
        """
        payload = cls.update_payload(
            payload=payload, last_user_id=last_user_id, **kwargs
        )
        return cls.model.objects.create(**payload)

    @classmethod
    def put(
        cls,
        *,
        instance: models.Model,
        payload: Dict,
        last_user_id: int,
        **kwargs,
    ) -> models.Model:
        """
        """
        if not isinstance(instance, cls.model):
            raise Http404(
                "The instance does not belong to the model."
                f"{cls.model._meta.verbose_name}."
            )

        payload = cls.update_payload(
            instance=instance,
            payload=payload,
            last_user_id=last_user_id,
            **kwargs,
        )
        for key, value in payload.items():
            setattr(instance, key, value)
        instance.save()

        return instance

    @classmethod
    def disable(
        cls, *, instance: models.Model, last_user_id: int
    ) -> models.Model:
        """
        """
        if not isinstance(instance, cls.model):
            raise Http404(
                "The instance does not belong to the model."
                f"{cls.model._meta.verbose_name}."
            )

        instance.is_active = False
        instance.last_user_id = last_user_id
        instance.save()
        return instance


class Service:
    """
    """

    repository: Repository
    whitelist_disable_models: List[Optional[str]] = []

    @classmethod
    def validate_payload(
        cls, *, payload: Dict[str, Any], id: Optional[int] = None, **kwargs
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        instance: Optional[models.Model] = None
        return status.HTTP_200_OK, instance

    @classmethod
    def list(cls, *, filters: Optional[Any] = None) -> models.QuerySet:
        queryset = cls.repository.list()
        if filters:
            queryset = filters.filter(queryset)
        return queryset

    @classmethod
    def get(cls, *, id: int, only: Optional[List[str]] = None) -> Tuple[int, models.Model | Dict[str, str]]:
        try:
            return status.HTTP_200_OK, cls.repository.get(id=id, only=only)
        except Http404:
            return status.HTTP_404_NOT_FOUND, {
                'message': (
                    f'{cls.repository.model._meta.verbose_name.capitalize()} '
                    'não existe.'
                )
            }

    @classmethod
    def post(
        cls, *, payload: Dict[str, Any], last_user_id: int, **kwargs
    ) -> Tuple[int, Union[models.Model, Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message: Dict[str, str]

                status_code, message = cls.validate_payload(payload=payload)
                if status_code != status.HTTP_200_OK:
                    return status_code, message

                instance = cls.repository.post(
                    payload=payload, last_user_id=last_user_id
                )
                return status.HTTP_201_CREATED, instance
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {
                'message': str(error)
            }

    @classmethod
    def put(
        cls, *, id: int, payload: Dict[str, Any], last_user_id: int, **kwargs
    ) -> Tuple[int, Union[models.Model, Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message: Dict[str, str]

                status_code, message_or_object = cls.validate_payload(
                    payload=payload, id=id
                )
                if status_code != status.HTTP_200_OK:
                    message: Dict = message_or_object
                    return status_code, message

                instance: models.Model = message_or_object

                instance = cls.repository.put(
                    instance=instance,
                    payload=payload,
                    last_user_id=last_user_id,
                )
                return status.HTTP_201_CREATED, instance
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {
                'message': str(error)
            }

    @classmethod
    def disable(
        cls, *, id: int, last_user_id: int
    ) -> Tuple[int, Union[models.Model, Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message_or_object: models.Model | Dict[str, str]

                status_code, message_or_object = cls.get(id=id)
                if status_code != status.HTTP_200_OK:
                    return status_code, message_or_object

                instance: models.Model = message_or_object

                if not instance.is_active:
                    verbose_name: str = (
                        cls.repository.model._meta.verbose_name.capitalize()
                    )
                    return status.HTTP_400_BAD_REQUEST, {
                        'message': (
                            f'{verbose_name} '
                            'está indisponível.'
                        )
                    }
                active_references: Union[list, str] = get_active_references(
                    model=instance,
                    whitelist=cls.whitelist_disable_models,
                )
                if active_references:
                    active_references = ', '.join(active_references)
                    verbose_name: str = (
                        cls.repository.model._meta.verbose_name.capitalize()
                    )
                    return status.HTTP_400_BAD_REQUEST, {
                        'message': (
                            f'Não é possível inativar {verbose_name}, '
                            'pois há as seguintes referências ativas: '
                            f'{active_references}.'
                        )
                    }

                instance = cls.repository.disable(
                    instance=instance, last_user_id=last_user_id
                )
                return status.HTTP_200_OK, instance
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {
                'message': str(error)
            }


class Controller:
    """
    """

    service: Service
