from app.platform_core.portfolio_intelligence.enterprise.performance import portfolio_enterprise_performance_gate
from app.platform_core.portfolio_intelligence.enterprise.quality_score import portfolio_enterprise_quality_score_service
from app.platform_core.portfolio_intelligence.enterprise.report import portfolio_enterprise_report_builder
from app.platform_core.portfolio_intelligence.enterprise.runtime_acceptance import portfolio_enterprise_runtime_acceptance
from app.platform_core.portfolio_intelligence.enterprise.security import portfolio_enterprise_security_gate
from app.platform_core.portfolio_intelligence.integration_report import portfolio_integration_report_service
from app.platform_core.portfolio_intelligence.analytics_service import portfolio_analytics_risk_service
from app.platform_core.portfolio_intelligence.service import portfolio_intelligence_core_service

class PortfolioEnterpriseService:
    def security(self): return portfolio_enterprise_security_gate.evaluate()
    def performance(self): return portfolio_enterprise_performance_gate.evaluate()
    def quality_score(self): return portfolio_enterprise_quality_score_service.calculate(security=self.security()["score"], performance=self.performance()["score"])
    def runtime_acceptance(self): return portfolio_enterprise_runtime_acceptance.contract()
    def final_report(self): return portfolio_enterprise_report_builder.build()
    def final_status(self):
        core = portfolio_intelligence_core_service.status()
        analytics = portfolio_analytics_risk_service.report()
        integration = portfolio_integration_report_service.report()
        quality = self.quality_score()
        return {"ready": core["ready"] and analytics["ready"] and integration["ready"] and quality["ready"], "core_ready": core["ready"], "analytics_ready": analytics["ready"], "integration_ready": integration["ready"], "quality_ready": quality["ready"], "quality_score": quality["overall"], "execution_allowed": False}
portfolio_enterprise_service = PortfolioEnterpriseService()
