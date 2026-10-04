from fastapi import APIRouter
from .profile.scrap import route as scrap_routes
from typing import Set

auth_router = APIRouter()

class Profile(BaseModel):
    id: int
    name: str
    linkedin: str
    github: str
    skills: Set[str]
    



@auth_router.post
def create_profile():
    


auth_router.include_router(
    scrap_routes,
    prefix="/scrap",
    tags=[]
)













# profile created - with email id and password
# resume parsing, linkedin parsing, github parsing, portfolio parsing, twitter parsing, interview transcripts, 
# extensive form fillup -  quick tests
# 