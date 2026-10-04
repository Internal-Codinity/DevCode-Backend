from fastapi import APIRouter

from app.schemas.auth import RegisterRequest

route = APIRouter()


@route.post("/")
def register(payload: RegisterRequest):
    return {
        "message": "User registered successfully",
        "name": payload.name,
        "email": payload.email,
    }
