class AIDecisionEventBuilder:
    def build(self, event_type: str, payload: dict, severity: str = "info"):
        return {"ready": True, "event_type": event_type, "payload": payload, "severity": severity}
ai_decision_event_builder = AIDecisionEventBuilder()
