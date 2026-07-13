from app.platform_core.portfolio_intelligence.action_plan import portfolio_action_plan_service
from app.platform_core.portfolio_intelligence.ai_link import portfolio_ai_link_service
from app.platform_core.portfolio_intelligence.decision_support import portfolio_decision_support_service
from app.platform_core.portfolio_intelligence.optimizer_link import portfolio_optimizer_link_service
from app.platform_core.portfolio_intelligence.risk_engine_link import portfolio_risk_engine_link_service

class PortfolioIntegrationReportService:
    def report(self):
        return {"ready": True, "ai_link": portfolio_ai_link_service.confidence_signal(), "optimizer_link": portfolio_optimizer_link_service.allocation_bias(), "risk_link": portfolio_risk_engine_link_service.risk_check(), "decision_support": portfolio_decision_support_service.recommendation(), "action_plan": portfolio_action_plan_service.plan(), "execution_allowed": False}

portfolio_integration_report_service = PortfolioIntegrationReportService()
