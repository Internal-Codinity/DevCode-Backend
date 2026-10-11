# app/api/v1/auth/route.py
from fastapi import APIRouter
from .login import route as login_routes
from .register import route as  register_routes

user_router = APIRouter()

user_router.include_router(
     login_routes,
     prefix="/login",
     tags=[login_routes.__name__]
)


user_router.include_router(
     register_routes,
     prefix="/register",
     tags=[register_routes.__name__]
)


user_router.include_router(
     logout_routes,
     prefix="/logout",
     tags=[logout_routes.__name__]
)

user_router.include_router(
     refresh_routes,
     prefix="/refresh",
     tags=[refresh_routes.__name__]
)



# auth setup, setup infra, setup redis, setup db, setup logger, setup config, setup env variables, setup error handling, setup middlewares, setup routes, setup tests