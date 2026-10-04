from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal
from app.services.code_run_service import code_run

code_router = APIRouter()

class CodeRunRequest(BaseModel):
    source: str
    language: Literal["python", "javascript"] = "javascript"

class CodeRunResponse(BaseModel):
    output: str
    success: bool

@code_router.post("/run", response_model=CodeRunResponse)
def run_code(payload: CodeRunRequest):
    if not payload.source.strip():
        raise HTTPException(status_code=400, detail="Source code is required")
    
    result = code_run(payload.source)
    return CodeRunResponse(
    output=result.stdout or "",
    success=True,
)

