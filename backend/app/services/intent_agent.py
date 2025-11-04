# intent_agent.py

def classify_intent(message: str) -> str:
    message = message.lower()
    if "refund" in message or "payment" in message:
        return "billing"
    elif "error" in message or "not working" in message:
        return "technical"
    elif "hello" in message or "hi" in message:
        return "greeting"
    else:
        return "general"
