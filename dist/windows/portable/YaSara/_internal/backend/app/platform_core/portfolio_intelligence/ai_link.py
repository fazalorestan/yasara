from app.platform_core.ai_decision.integration.service import ai_decision_integration_service

class PortfolioAILinkService:
    def decision_context(self):
        decision = ai_decision_integration_service.decision()
        return {"ready": decision["ready"], "ai_decision": decision["decision"], "source": "ai_decision_engine", "execution_allowed": False}

    def confidence_signal(self):
        decision = self.decision_context()["ai_decision"]
        confidence = float(decision.get("confidence", 0.0))
        signal = "strong" if confidence >= 75 else "moderate" if confidence >= 50 else "weak"
        return {"ready": True, "confidence": confidence, "signal_strength": signal, "execution_allowed": False}

portfolio_ai_link_service = PortfolioAILinkService()
