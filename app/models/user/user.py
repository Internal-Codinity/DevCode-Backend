from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True


