from typing import Set

from fastapi import APIRouter
from pydantic import BaseModel

from .scrap import route as scrap_routes

profile_router = APIRouter()


class Profile(BaseModel):
    id: int
    name: str
    linkedin: str
    github: str
    skills: Set[str]


@profile_router.post("/")
def create_profile(payload: Profile):
    return payload


profile_router.include_router(
    scrap_routes,
    prefix="/scrap",
    tags=[]
)













# profile created - with email id and password
# resume parsing, linkedin parsing, github parsing, portfolio parsing, twitter parsing, interview transcripts, 
# extensive form fillup -  quick tests
# 