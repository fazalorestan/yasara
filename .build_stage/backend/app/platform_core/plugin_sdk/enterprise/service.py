from app.platform_core.plugin_sdk.enterprise.performance import plugin_enterprise_performance_gate
from app.platform_core.plugin_sdk.enterprise.quality_score import plugin_enterprise_quality_score_service
from app.platform_core.plugin_sdk.enterprise.report import plugin_enterprise_report_builder
from app.platform_core.plugin_sdk.enterprise.runtime_acceptance import plugin_enterprise_runtime_acceptance
from app.platform_core.plugin_sdk.enterprise.security import plugin_enterprise_security_gate
from app.platform_core.plugin_sdk.runtime_report import plugin_runtime_report_service
from app.platform_core.plugin_sdk.service import plugin_sdk_core_service
from app.platform_core.plugin_sdk.versioning_report import plugin_versioning_report_service

class PluginEnterpriseService:
    def security(self): return plugin_enterprise_security_gate.evaluate()
    def performance(self): return plugin_enterprise_performance_gate.evaluate()
    def quality_score(self):
        return plugin_enterprise_quality_score_service.calculate(
            security=self.security()["score"],
            performance=self.performance()["score"],
        )
    def runtime_acceptance(self): return plugin_enterprise_runtime_acceptance.contract()
    def final_report(self): return plugin_enterprise_report_builder.build()
    def final_status(self):
        core = plugin_sdk_core_service.status()
        runtime = plugin_runtime_report_service.report()
        versioning = plugin_versioning_report_service.report()
        quality = self.quality_score()
        return {
            "ready": core["ready"] and runtime["ready"] and versioning["ready"] and quality["ready"],
            "core_ready": core["ready"],
            "runtime_ready": runtime["ready"],
            "versioning_ready": versioning["ready"],
            "quality_ready": quality["ready"],
            "quality_score": quality["overall"],
            "execution_allowed": False,
        }

plugin_enterprise_service = PluginEnterpriseService()
