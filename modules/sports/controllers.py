from typing import Any, Tuple

from django.db.models import QuerySet
from ninja import Query
from ninja_extra import api_controller, paginate, route
from ninja_extra.ordering import Ordering, ordering
from core.schemas import CustomPagination, MessageSchema, PaginatedResponseSchema
from core.utils.classes import Controller
from core.utils.constants import ERROR_STATUSES, SUCCESS_STATUSES
from modules.sports.services import SportsService
from .schemas import   SportsFilter, SportsInPost, SportsInPut, SportsList, SportsOut


@api_controller(
    'sports/',
    tags=['SPORTS - CORE CRUD OF SPORTS'],
    
)
class SportsController(Controller):
    """
    Controller responsável por gerenciar as operações CRUD dos esportes.
    """

    service = SportsService

    @route.post(
        '/',
        response={
            SUCCESS_STATUSES: SportsOut,
            ERROR_STATUSES: MessageSchema,
        },
        # permissions=[PostWasteTreatmentsAccess],
    )
    def post(self, request, payload: SportsInPost) -> Tuple[Any, ...]:
        """
        """
        return self.service.post(
            payload=payload.dict(),
            last_user_id=request.user.id,
        )

    @route.get(
        'sports/',
        response=PaginatedResponseSchema[SportsList],
        # permissions=[GetUsersAccess],
    )
    @paginate(CustomPagination)
    @ordering(
        Ordering,
        ordering_fields=[
            'id',
            'name',],
    )
    def list(self, filters: SportsFilter = Query(...)) -> QuerySet[Any]:
        """
        ----------------------------------------------
        """
        return self.service.list(filters=filters)

    @route.get(
        'sports/{int:id}',
        response={
            SUCCESS_STATUSES: SportsOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def get(
        self,
        id: int,  
    ) -> Tuple[Any, ...]:
        """
        -------------------------------------
        """
        return self.service.get(id=id)

    @route.put(
        "sports/{int:id}",
        response={
            SUCCESS_STATUSES: SportsOut,
            ERROR_STATUSES: MessageSchema,
        },
        # permissions=[PutVehiclesAccess],
    )
    def put(self, request, id: int, payload: SportsInPut) -> Tuple[Any, ...]:
        """
        Rota responsável pelo atualização de veículos.
        -----------------------------------------------------------------------------
        """
        return self.service.put(id=id, payload=payload.dict(), last_user_id=request.user.id)
    
    @route.patch(
        "sports/{int:id}/disable/",
        response={
            SUCCESS_STATUSES: SportsOut,
            ERROR_STATUSES: MessageSchema,
        },
        # permissions=[DisableVehiclesAccess],
    )
    def disable(
        self,
        request,
        id: int,
    ) -> Tuple[Any, ...]:
        """

        """
        return self.service.disable(
            id=id,
            last_user_id=request.user.id,
        )
        