from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None


class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool


class UserInDB(UserRead):
    hashed_password: str


# user schemas, user create, user read, user in db, user update, user delete, user deactivate, user activate, user exists --- IGNORE ---