from dataclasses import dataclass
from typing import Optional
from app.database.base import Base


@dataclass
class User(Base):
    id: int
    email: str
    hashed_password: str
    full_name: Optional[str] = None
    user_name: Optional[str] = None
    bio: Optional[str] = None
    job_title: Optional[str] = None
    graduation_year: Optional[int] = None
    most_recent_job: Optional[str] = None
    preferred_language: Optional[list[str]] = None
    url: Optional[list[str]] = None
    university: Optional[str] = None
    skills: Optional[list[str]] = None
    is_active: bool = True