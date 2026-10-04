from typing import List, Optional

from app.models.user.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository | None = None):
        self.repository = repository or UserRepository()

    def get_user(self, email: str) -> Optional[User]:
        return self.repository.get_by_email(email)

    def all_users(self) -> List[User]:
        return self.repository.list_users()



# user service, get user by email, list all users, delete user by email, update user, deactivate user, activate user, check if user exists