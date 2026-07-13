from app.platform_core.portfolio_intelligence.decision_support import portfolio_decision_support_service
from app.platform_core.portfolio_intelligence.service import portfolio_intelligence_core_service

class PortfolioActionPlanService:
    def plan(self):
        recommendation = portfolio_decision_support_service.recommendation()
        rebalance = portfolio_intelligence_core_service.rebalance()
        return {"ready": True, "recommendation": recommendation["action"], "rebalance_actions": rebalance["actions"], "requires_human_confirmation": True, "execution_allowed": False}

portfolio_action_plan_service = PortfolioActionPlanService()
