from app.v52_ai_decision_engine.dependency import get_service

class AIDecisionFacade:
    def decide(self, payload):
        result = get_service("ai_decision.fusion").fuse(payload)
        result.explanation = get_service("ai_decision.explain").explain(result)
        result.strategy_alignment = get_service("ai_decision.strategy").align(result)
        get_service("ai_decision.timeline").append(result)
        return result
    def confirmations(self, payload):
        svc = get_service("ai_decision.confirmation")
        return {"confirmed": svc.confirmed(payload.evidences), "rejected": svc.rejected(payload.evidences)}
    def timeline(self, limit=100):
        return get_service("ai_decision.timeline").list(limit)
    def keylevels(self, payload):
        return get_service("ai_decision.keylevels").normalize(payload)
    def doctor(self):
        deps = {k: get_service(k) for k in [
            "ai_decision.fusion","ai_decision.confirmation","ai_decision.explain",
            "ai_decision.strategy","ai_decision.timeline","ai_decision.keylevels"
        ]}
        return get_service("ai_decision.doctor").health(deps)

ai_decision_facade = AIDecisionFacade()
