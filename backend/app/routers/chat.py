# backend/app/routers/chat.py

from fastapi import APIRouter
from app.services.intent_agent import classify_intent
from app.services.knowledge_agent import generate_response
from app.services.escalation_agent import check_escalation
from app.models import ChatRequest, ChatResponse

router = APIRouter()  # <-- this must be defined

@router.post("/", response_model=ChatResponse)
def chat_route(request: ChatRequest):
    intent = classify_intent(request.message)
    response = generate_response(request.message, intent)

    if check_escalation(response):
        return ChatResponse(reply="Escalating to human support...")

    return ChatResponse(reply=response)
@router.get("/")
def root():
    return {"message": "Multi-agent system up!"}

