from app.platform_core.portfolio_intelligence.ai_link import portfolio_ai_link_service
from app.platform_core.portfolio_intelligence.optimizer_link import portfolio_optimizer_link_service
from app.platform_core.portfolio_intelligence.risk_engine_link import portfolio_risk_engine_link_service

class PortfolioDecisionSupportService:
    def recommendation(self):
        ai = portfolio_ai_link_service.confidence_signal()
        opt = portfolio_optimizer_link_service.allocation_bias()
        risk = portfolio_risk_engine_link_service.risk_check()
        if not risk["allowed"]:
            action = "reduce_risk"
        elif ai["signal_strength"] == "strong" and opt["bias"] == "increase":
            action = "increase_allocation"
        elif ai["signal_strength"] == "weak":
            action = "hold"
        else:
            action = "rebalance_only"
        return {"ready": True, "action": action, "ai": ai, "optimizer": opt, "risk": risk, "execution_allowed": False}

portfolio_decision_support_service = PortfolioDecisionSupportService()
