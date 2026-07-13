from app.v52_ai_decision_engine.models import DecisionResult

class ExplainService:
    def explain(self, result: DecisionResult):
        lines = [f"Decision: {result.decision.value}"]
        lines += [f"{e.source}: {e.reason or 'confirmed'}" for e in result.confirmations]
        lines.append(f"Confidence: {round(result.confidence * 100, 2)}%")
        return lines
