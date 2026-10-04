from fastapi import APIRouter

route = APIRouter()


@route.get("/")
def scrap_profile():
    return {"message": "Scraping not implemented yet"}
