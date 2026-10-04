# app/api/v1/auth/route.py
from fastapi import APIRouter
from .login import route as login_routes
from .register import route as  register_routes

auth_router = APIRouter()

auth_router.include_router(
     login_routes,
     prefix="/login",
     tags=[]
)


auth_router.include_router(
     register_routes,
     prefix="/register"
     tags=[]
)




# auth setup, setup infra, setup redis, setup db, setup logger, setup config, setup env variables, setup error handling, setup middlewares, setup routes, setup tests