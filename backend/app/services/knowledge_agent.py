# knowledge_agent.py

def generate_response(message: str, intent: str) -> str:
    if intent == "billing":
        return "You can expect your refund within 5–7 business days."
    elif intent == "technical":
        return "Please try restarting your device and updating the software."
    elif intent == "greeting":
        return "Hi there! How can I assist you today?"
    else:
        return "I'm not sure I understand. Would you like me to connect you to a human agent?"
