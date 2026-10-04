from typing import Dict, Optional

from app.models.user.user import User


class UserRepository:
    _storage: Dict[str, User] = {}

    def create(self, user: User) -> User:
        self._storage[user.email] = user
        return user

    def get_by_email(self, email: str) -> Optional[User]:
        return self._storage.get(email)

    def list_users(self) -> list[User]:
        return list(self._storage.values())
    
    def delete_by_email(self, email: str) -> bool:
        if email in self._storage:
            del self._storage[email]
            return True
        return False
    
    def update_user(self, email: str, updated_user: User) -> Optional[User]:
        if email in self._storage:
            self._storage[email] = updated_user
            return updated_user
        return None
    
    def deactivate_user(self, email: str) -> Optional[User]:
        user = self._storage.get(email)
        if user:
            user.is_active = False
            self._storage[email] = user
            return user
        return None
    
    def activate_user(self, email: str) -> Optional[User]:
        user = self._storage.get(email)
        if user:
            user.is_active = True
            self._storage[email] = user
            return user
        return None
    
    def user_exists(self, email: str) -> bool:
        return email in self._storage   
    

# user repository, create user, get user by email, list users, delete user by email, update user, deactivate user, activate user, check if user exists