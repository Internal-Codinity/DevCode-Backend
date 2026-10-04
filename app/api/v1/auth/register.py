from fastapi import APIRouter, HTTPException, status


route = APIRouter()

@route.post("/register")
def register(Name:str, Email:str, Phone:int)
    
    
