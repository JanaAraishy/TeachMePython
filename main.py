from fastapi import FastAPI
from pydantic import BaseModel

from rag import ask_rag
from db import save_chat, save_user

app = FastAPI()

# ------------------------------------------------
# MODELS
# ------------------------------------------------

class QuestionRequest(BaseModel):
    question: str
    user_id: int


class AnswerResponse(BaseModel):
    answer: str


class UserName(BaseModel):
    name: str
    level: int


class LoginResponse(BaseModel):
    user_id: int
    name: str


# ------------------------------------------------
# LOGIN
# ------------------------------------------------

@app.post("/login")
def login(request: UserName):

    user_id = save_user(
        request.name,
        request.level
    )

    return {
        "user_id": user_id,
        "name": request.name
    }


# ------------------------------------------------
# ASK QUESTION
# ------------------------------------------------

@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    response = ask_rag(request.question)

    save_chat(
        request.user_id,
        request.question,
        response
    )

    return {
        "answer": response
    }