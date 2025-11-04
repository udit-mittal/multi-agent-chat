# escalation_agent.py

def check_escalation(response: str) -> bool:
    # Escalate if bot is unsure
    return "not sure" in response.lower() or "connect" in response.lower()
