from app.platform_core.ai_decision.integration.service import ai_decision_integration_service
class AIDecisionIntegrationReadinessGate:
    def run(self):
        evidence = ai_decision_integration_service.integrated_evidence()
        decision = ai_decision_integration_service.decision()
        status = ai_decision_integration_service.status()
        ready = evidence["ready"] and decision["ready"] and status["ready"]
        return {"ready": ready, "checks": {"evidence_ready": evidence["ready"], "decision_ready": decision["ready"], "status_ready": status["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
ai_decision_integration_readiness_gate = AIDecisionIntegrationReadinessGate()
