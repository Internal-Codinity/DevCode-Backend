from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

questions_router = APIRouter()

class Question(BaseModel):
    id: int
    title: str
    body: str

class CreateQuestionRequest(BaseModel):
    title: str
    body: str

QUESTIONS: List[Question] = []

@questions_router.get("/", response_model=List[Question])
def list_questions():
    return QUESTIONS

@questions_router.post("/", response_model=Question)
def create_question(payload: CreateQuestionRequest):
    question = Question(id=len(QUESTIONS) + 1, title=payload.title, body=payload.body)
    QUESTIONS.append(question)
    return question
