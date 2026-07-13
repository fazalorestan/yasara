class AIDecisionEventBusContract:
    def publish_contract(self, event: dict):
        return {"ready": True, "published": False, "dry_run": True, "event": event, "reason": "event_bus_contract_only"}
    def topics(self):
        return {"ready": True, "topics": ["ai.decision.created", "ai.decision.rejected", "ai.decision.quality_failed"]}
ai_decision_event_bus_contract = AIDecisionEventBusContract()
