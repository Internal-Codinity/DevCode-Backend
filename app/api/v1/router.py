from fastapi import APIRouter

from .auth.route import auth_router
from .code.route import code_router
from .questions.route import questions_router
from .profile.route import profile_router

api_router = APIRouter()

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

api_router.include_router(
    code_router,
    prefix="/code",
    tags=["Code"]
)

api_router.include_router(
    questions_router,
    prefix="/questions",
    tags=["Questions"]
)

api_router.include_router(
    profile_router,
    prefix="/profile",
    tags=["Profile"]
)


# api setup, setup infra, setup redis, setup db, setup logger, setup config, setup env variables, setup error handling, setup middlewares, setup routes, setup tests