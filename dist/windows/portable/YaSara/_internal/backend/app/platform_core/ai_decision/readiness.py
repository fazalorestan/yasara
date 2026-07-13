from app.platform_core.ai_decision.service import ai_decision_core_service
class AIDecisionCoreReadinessGate:
    def run(self):
        trace = ai_decision_core_service.trace()
        metrics = ai_decision_core_service.metrics()
        safety = ai_decision_core_service.safety()
        ready = trace["ready"] and metrics["ready"] and safety["ready"]
        return {"ready": ready, "checks": {"trace_ready": trace["ready"], "metrics_ready": metrics["ready"], "safety_ready": safety["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
ai_decision_core_readiness_gate = AIDecisionCoreReadinessGate()
