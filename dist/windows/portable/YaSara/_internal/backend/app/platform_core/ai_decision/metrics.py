class AIDecisionMetricsService:
    def summarize(self, decisions: list[dict]):
        total = len(decisions)
        avg_confidence = 0.0 if total == 0 else sum(float(x.get("confidence", 0.0)) for x in decisions) / total
        blocked = len([x for x in decisions if x.get("execution_allowed") is False])
        return {"ready": True, "total_decisions": total, "avg_confidence": avg_confidence, "blocked_decisions": blocked, "execution_allowed": False}
ai_decision_metrics_service = AIDecisionMetricsService()
