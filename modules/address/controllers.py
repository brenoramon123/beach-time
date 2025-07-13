from typing import Any, List, Tuple

from django.db.models import QuerySet
from ninja import Query
from ninja_extra import api_controller, paginate, route
from ninja_extra.ordering import Ordering, ordering

from core.schemas import CustomPagination, MessageSchema, PaginatedResponseSchema
from core.utils.classes import Controller
from core.utils.constants import ERROR_STATUSES, SUCCESS_STATUSES

from .schemas import (
    CityFilter,
    CityInPost,
    CityInPut,
    CityList,
    CityOut,
    CountryFilter,
    CountryInPost,
    CountryInPut,
    CountryList,
    CountryOut,
    FederativeUnitFilter,
    FederativeUnitInPost,
    FederativeUnitInPut,
    FederativeUnitList,
    FederativeUnitOut
)
from .services import (
    CityServices,
    CountryServices,
    FederativeUnitServices,
)


@api_controller(
    'core/addresses/',
    tags=['CORE - ADDRESSES'],
    
)
class CountryController(Controller):
    """
    Responsável por controlar as requisições relacionadas ao submódulo de país,
    a qual as recebe e coordena as ações necessárias.
    """

    service: CountryServices = CountryServices

    @route.get(
        'country/',
        response=PaginatedResponseSchema[CountryList],
        auth=None,

    )
    @paginate(CustomPagination)
    @ordering(
        Ordering,
        ordering_fields=[
            'id',
            'name',
            'abbreviation',
        ],
    )
    def list(
        self,
        filters: CountryFilter = Query(...),
    ) -> QuerySet[Any]:
        """

        """
        return self.service.list(filters=filters)

    @route.get(
        'country/{int:id}',
        response={
            SUCCESS_STATUSES: CountryOut,
            ERROR_STATUSES: MessageSchema,
        },

    )
    def get(
        self,
        id: int,  
    ) -> Tuple[Any, ...]:
        """
 
        """
        return self.service.get(id=id)

    @route.post(
        'country/',
        response={
            SUCCESS_STATUSES: CountryOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def post(self, request, payload: CountryInPost) -> Tuple[Any, ...]:
        """

        """
        return self.service.post(
            payload=payload.dict(),
            last_user_id=request.user.id,
        )
    

    @route.post('/multiples',         
                response={
            SUCCESS_STATUSES: List[CountryList],
            ERROR_STATUSES: MessageSchema,
        },)
    def create_multiple_countries(self, request, payload: List[CountryInPost]):
        last_user_id = request.user.id

        payload_list = [country.dict() for country in payload]

        return self.service.multiples(payload=payload_list, last_user_id=last_user_id)
    @route.put(
        'country/{int:id}',
        response={
            SUCCESS_STATUSES: CountryOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def put(
        self,
        request,
        id: int,  
        payload: CountryInPut,
    ) -> Tuple[Any, ...]:
        """

        """
        return self.service.put(
            id=id,
            payload=payload.dict(),
            last_user_id=request.user.id,
        )

    @route.patch(
        'country/{int:id}/disable/',
        response={
            SUCCESS_STATUSES: CountryOut,
            ERROR_STATUSES: MessageSchema,
        },
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


@api_controller(
    'core/addresses/',
    tags=['CORE - ADDRESSES'],
    
)
class FederativeUnitController(Controller):
    """

    """

    service: FederativeUnitServices = FederativeUnitServices

    @route.get(
        'federative-unit/',
        response=PaginatedResponseSchema[FederativeUnitList],
        auth=None,

    )
    @paginate(CustomPagination)
    @ordering(
        Ordering,
        ordering_fields=[
            'id',
            'name',
            'abbreviation',
            'country__name',
        ],
    )
    def list(
        self, filters: FederativeUnitFilter = Query(...)
    ) -> QuerySet[Any]:
        """
 
        """
        return self.service.list(filters=filters)

    @route.get(
        'federative-unit/{int:id}',
        response={
            SUCCESS_STATUSES: FederativeUnitOut,
            ERROR_STATUSES: MessageSchema,
        }
    )
    def get(
        self,
        id: int,  
    ) -> Tuple[Any, ...]:
        """

        """
        return self.service.get(id=id)

    @route.post(
        'federative-unit/',
        response={
            SUCCESS_STATUSES: FederativeUnitOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def post(self, request, payload: FederativeUnitInPost) -> Tuple[Any, ...]:
        """

        """
        return self.service.post(
            payload=payload.dict(),
            last_user_id=request.user.id,
        )

    @route.put(
        'federative-unit/{int:id}',
        response={
            SUCCESS_STATUSES: FederativeUnitOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def put(
        self,
        request,
        id: int,  
        payload: FederativeUnitInPut,
    ) -> Tuple[Any, ...]:
        """

        """
        return self.service.put(
            id=id,
            payload=payload.dict(),
            last_user_id=request.user.id,
        )

    @route.patch(
        'federative-unit/{int:id}/disable/',
        response={
            SUCCESS_STATUSES: FederativeUnitOut,
            ERROR_STATUSES: MessageSchema,
        },
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


@api_controller(
    'core/addresses/',
    tags=['CORE - ADDRESSES'],
)
class CityController(Controller):
    """

    """

    service: CityServices = CityServices

    @route.get(
        'city/',
        response=PaginatedResponseSchema[CityList],
        auth=None,
    )
    @paginate(CustomPagination)
    @ordering(
        Ordering,
        ordering_fields=[
            'id',
            'name',
            'federative_unit__name',
        ],
    )
    def list(self, filters: CityFilter = Query(...)) -> QuerySet[Any]:
        """

        """
        return self.service.list(filters=filters)

    @route.get(
        'city/{int:id}',
        response={
            SUCCESS_STATUSES: CityOut,
            ERROR_STATUSES: MessageSchema,
        }
    )
    def get(
        self,
        id: int,  
    ) -> Tuple[Any, ...]:
        """

        """
        return self.service.get(id=id)

    @route.post(
        'city/',
        response={
            SUCCESS_STATUSES: CityOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def post(self, request, payload: CityInPost) -> Tuple[Any, ...]:
        """

        """
        return self.service.post(
            payload=payload.dict(),
            last_user_id=request.user.id,
        )

    @route.put(
        'city/{int:id}',
        response={
            SUCCESS_STATUSES: CityOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def put(self, request, id: int, payload: CityInPut) -> Tuple[Any, ...]:  
        """

        """
        return self.service.put(
            id=id,
            payload=payload.dict(),
            last_user_id=request.user.id,
        )

    @route.patch(
        'city/{int:id}/disable/',
        response={
            SUCCESS_STATUSES: CityOut,
            ERROR_STATUSES: MessageSchema,
        },
    )
    def disable(
        self,
        request,
        id: int,  
    ) -> Tuple[Any, ...]:
        """

        """
        return self.service.disable(id=id, last_user_id=request.user.id)