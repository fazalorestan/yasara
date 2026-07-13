from app.platform_core.ai_decision.pipeline import ai_decision_pipeline
from app.platform_core.ai_decision.integration.alert_link import ai_decision_alert_link
from app.platform_core.ai_decision.integration.event_bus import ai_decision_event_bus_contract
from app.platform_core.ai_decision.integration.logging import ai_decision_logging_contract
from app.platform_core.ai_decision.integration.optimizer_link import ai_decision_optimizer_link
from app.platform_core.ai_decision.integration.portfolio_link import ai_decision_portfolio_link
from app.platform_core.ai_decision.integration.risk_link import ai_decision_risk_link
from app.platform_core.ai_decision.integration.scanner_link import ai_decision_scanner_link
class AIDecisionIntegrationService:
    def context(self):
        return {"symbol": "BTCUSDT", "timeframe": "1h", "signal_source": "integration", "market_regime": "trend", "risk_state": ai_decision_portfolio_link.portfolio_state()["state"]}
    def integrated_evidence(self):
        evidence = []
        evidence.extend(ai_decision_scanner_link.evidence()["evidence"])
        evidence.extend(ai_decision_optimizer_link.evidence()["evidence"])
        evidence.extend(ai_decision_risk_link.evidence()["evidence"])
        return {"ready": True, "evidence": evidence, "count": len(evidence), "execution_allowed": False}
    def decision(self):
        return ai_decision_pipeline.run(self.context(), self.integrated_evidence()["evidence"])
    def event_bus(self):
        return ai_decision_event_bus_contract.publish_contract({"type": "ai_decision_integration", "decision": self.decision()["decision"]})
    def logging(self):
        d = self.decision()
        return ai_decision_logging_contract.log_decision({"decision_id": "ai_integration_decision", "confidence": d["decision"]["confidence"]})
    def alert(self): return ai_decision_alert_link.alert_contract()
    def status(self):
        d, e, l = self.decision(), self.event_bus(), self.logging()
        return {"ready": d["ready"] and e["ready"] and l["ready"], "decision_ready": d["ready"], "event_bus_ready": e["ready"], "logging_ready": l["ready"], "execution_allowed": False}
ai_decision_integration_service = AIDecisionIntegrationService()
