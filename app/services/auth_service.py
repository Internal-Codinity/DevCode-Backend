from typing import Optional

from app.core.security import verify_password, create_access_token, hash_password
from app.models.user.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository | None = None):
        self.repository = repository or UserRepository()

    def authenticate_user(self, email: str, password: str) -> Optional[str]:
        user = self.repository.get_by_email(email)
        if user and verify_password(password, user.hashed_password):
            return create_access_token(subject=user.email)
        return None

    def register_user(self, email: str, password: str, full_name: str | None = None) -> User:
        hashed = hash_password(password)
        user = User(id=len(self.repository.list_users()) + 1, email=email, hashed_password=hashed, full_name=full_name)
        return self.repository.create(user)
