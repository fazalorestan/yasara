from app.platform_core.portfolio_intelligence.action_plan import portfolio_action_plan_service
from app.platform_core.portfolio_intelligence.ai_link import portfolio_ai_link_service
from app.platform_core.portfolio_intelligence.decision_support import portfolio_decision_support_service
from app.platform_core.portfolio_intelligence.integration_readiness import portfolio_integration_readiness_gate
from app.platform_core.portfolio_intelligence.integration_report import portfolio_integration_report_service
from app.platform_core.portfolio_intelligence.optimizer_link import portfolio_optimizer_link_service
from app.platform_core.portfolio_intelligence.risk_engine_link import portfolio_risk_engine_link_service
from app.v500_alpha35_portfolio_ai_optimization.models import PortfolioAIOptimizationSummaryV500Alpha35

class PortfolioAIOptimizationFacadeV500Alpha35:
    def summary(self): return PortfolioAIOptimizationSummaryV500Alpha35()
    def ai_decision(self): return portfolio_ai_link_service.decision_context()
    def ai_signal(self): return portfolio_ai_link_service.confidence_signal()
    def optimizer_best(self): return portfolio_optimizer_link_service.optimizer_best()
    def allocation_bias(self): return portfolio_optimizer_link_service.allocation_bias()
    def risk_check(self): return portfolio_risk_engine_link_service.risk_check()
    def recommendation(self): return portfolio_decision_support_service.recommendation()
    def action_plan(self): return portfolio_action_plan_service.plan()
    def report(self): return portfolio_integration_report_service.report()
    def readiness(self): return portfolio_integration_readiness_gate.run()
    def contract(self): return {"ready": True, "portfolio_intelligence": "package_c_ai_optimization_link", "execution_allowed": False}
