from app.platform_core.ai_decision.enterprise.performance import ai_decision_performance_gate
from app.platform_core.ai_decision.enterprise.quality_score import ai_decision_quality_score_service
from app.platform_core.ai_decision.enterprise.report import ai_decision_sprint_report_builder
from app.platform_core.ai_decision.enterprise.runtime_acceptance import ai_decision_final_runtime_acceptance
from app.platform_core.ai_decision.enterprise.security import ai_decision_security_gate
from app.platform_core.ai_decision.integration.service import ai_decision_integration_service
from app.platform_core.ai_decision.services_package_b import ai_decision_services_package_b
from app.platform_core.ai_decision.service import ai_decision_core_service

class AIDecisionEnterpriseService:
    def security(self): return ai_decision_security_gate.evaluate()
    def performance(self): return ai_decision_performance_gate.evaluate()
    def quality_score(self): return ai_decision_quality_score_service.calculate(security=self.security()["score"], performance=self.performance()["score"])
    def runtime_acceptance(self): return ai_decision_final_runtime_acceptance.contract()
    def sprint_report(self): return ai_decision_sprint_report_builder.build()
    def final_status(self):
        core = ai_decision_core_service.trace()
        services = ai_decision_services_package_b.status()
        integration = ai_decision_integration_service.status()
        quality = self.quality_score()
        return {"ready": core["ready"] and services["ready"] and integration["ready"] and quality["ready"], "core_ready": core["ready"], "services_ready": services["ready"], "integration_ready": integration["ready"], "quality_ready": quality["ready"], "quality_score": quality["overall"], "execution_allowed": False}
ai_decision_enterprise_service = AIDecisionEnterpriseService()
