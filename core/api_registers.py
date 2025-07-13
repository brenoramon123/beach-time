from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja import Swagger
from django.conf import settings

from modules.sports.controllers import SportsController
from modules.tokens.controllers import TokenJWTController
from modules.users.controllers import UserController



api = NinjaExtraAPI(
    auth=JWTAuth(),
    title=f"{settings.SYSTEM_NAME.upper()} - API",
    version=f"{settings.SYSTEM_VERSION}",
    description=f"{settings.SYSTEM_DESCRIPTION}",
    app_name=f"{settings.SYSTEM_NAME}",
    docs_url=settings.API_DOC_URL,
    docs=Swagger(
        settings={
            "docExpansion": "none",
            "tagsSorter": "alpha",
            "filter": True,
            "syntaxHighlight": {
                "activate": True,
                "theme": "nord",
            },
            "persistAuthorization": True,
        }
    ),
)

# CORE REGISTRATIONS:
api.register_controllers(
    TokenJWTController,
    UserController
)

# SPORTS REGISTRATIONS:
api.register_controllers(
    SportsController,
)
