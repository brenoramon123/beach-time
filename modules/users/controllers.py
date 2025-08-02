from typing import Any, Tuple

from django.db.models import QuerySet
from ninja import File, Query, UploadedFile
from ninja_extra import api_controller, paginate, route
from ninja_extra.ordering import Ordering, ordering

from core.schemas import CustomPagination, MessageSchema, PaginatedResponseSchema
from core.utils.classes import Controller
from core.utils.constants import ERROR_STATUSES, SUCCESS_STATUSES

from .schemas import UserFilter, UserList, UserOut, UserPostSchema
from .services import UserService


@api_controller(
    'core/',
    tags=['CORE - USERS'],
    
)
class UserController(Controller):
    """
    Responsável por controlar as requisições relacionadas ao submódulo de usuários,
    a qual as recebe e coordena as ações necessárias.
    """

    service = UserService
    @route.post('', response={
            SUCCESS_STATUSES: UserOut,
            ERROR_STATUSES: MessageSchema,
        }, auth=None)
    def post(self, request, payload: UserPostSchema, profile_picture: UploadedFile = File(None)):
        
        return self.service.post(payload=payload.dict(), file=profile_picture)
    
    @route.get(
        'users/',
        response=PaginatedResponseSchema[UserList],
        # permissions=[GetUsersAccess],
    )
    @paginate(CustomPagination)
    @ordering(
        Ordering,
        ordering_fields=[
            'id',
            'username',        ],
    )
    def list(self, filters: UserFilter = Query(...)) -> QuerySet[Any]:
        """

        """
        return self.service.list(filters=filters)

    @route.get(
        'user/{int:id}',
        response={
            SUCCESS_STATUSES: UserOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def get(
        self,
        id: int,  
    ) -> Tuple[Any, ...]:
        """
        Retorna um usuário pelo ID informado.
        -------------------------------------
        """
        return self.service.get(id=id)

