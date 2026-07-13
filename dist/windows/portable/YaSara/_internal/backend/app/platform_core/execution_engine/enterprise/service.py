from app.platform_core.execution_engine.analytics_report import execution_analytics_report
from app.platform_core.execution_engine.enterprise.performance import execution_enterprise_performance_gate
from app.platform_core.execution_engine.enterprise.quality_score import execution_enterprise_quality_score_service
from app.platform_core.execution_engine.enterprise.report import execution_enterprise_report_builder
from app.platform_core.execution_engine.enterprise.runtime_acceptance import execution_enterprise_runtime_acceptance
from app.platform_core.execution_engine.enterprise.security import execution_enterprise_security_gate
from app.platform_core.execution_engine.lifecycle_report import execution_lifecycle_report
from app.platform_core.execution_engine.report import execution_core_report
from app.platform_core.execution_engine.routing_report import order_routing_report

class ExecutionEnterpriseService:
    def security(self): return execution_enterprise_security_gate.evaluate()
    def performance(self): return execution_enterprise_performance_gate.evaluate()
    def quality_score(self):
        return execution_enterprise_quality_score_service.calculate(
            security=self.security()["score"],
            performance=self.performance()["score"],
        )
    def runtime_acceptance(self): return execution_enterprise_runtime_acceptance.contract()
    def final_report(self): return execution_enterprise_report_builder.build()
    def final_status(self):
        core = execution_core_report.report()
        routing = order_routing_report.report()
        lifecycle = execution_lifecycle_report.report()
        analytics = execution_analytics_report.report()
        quality = self.quality_score()
        return {
            "ready": core["ready"] and routing["ready"] and lifecycle["ready"] and analytics["ready"] and quality["ready"],
            "core_ready": core["ready"],
            "routing_ready": routing["ready"],
            "lifecycle_ready": lifecycle["ready"],
            "analytics_ready": analytics["ready"],
            "quality_ready": quality["ready"],
            "quality_score": quality["overall"],
            "execution_allowed": False,
        }

execution_enterprise_service = ExecutionEnterpriseService()
