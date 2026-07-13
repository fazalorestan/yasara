from app.platform_core.live_data_pipeline.cache_report import live_data_cache_report_service
from app.platform_core.live_data_pipeline.enterprise.performance import live_data_enterprise_performance_gate
from app.platform_core.live_data_pipeline.enterprise.quality_score import live_data_enterprise_quality_score_service
from app.platform_core.live_data_pipeline.enterprise.report import live_data_enterprise_report_builder
from app.platform_core.live_data_pipeline.enterprise.runtime_acceptance import live_data_enterprise_runtime_acceptance
from app.platform_core.live_data_pipeline.enterprise.security import live_data_enterprise_security_gate
from app.platform_core.live_data_pipeline.report import live_data_pipeline_core_report
from app.platform_core.live_data_pipeline.stream_report import live_stream_manager_report

class LiveDataEnterpriseService:
    def security(self): return live_data_enterprise_security_gate.evaluate()
    def performance(self): return live_data_enterprise_performance_gate.evaluate()
    def quality_score(self):
        return live_data_enterprise_quality_score_service.calculate(
            security=self.security()["score"],
            performance=self.performance()["score"],
        )
    def runtime_acceptance(self): return live_data_enterprise_runtime_acceptance.contract()
    def final_report(self): return live_data_enterprise_report_builder.build()
    def final_status(self):
        core = live_data_pipeline_core_report.report()
        stream = live_stream_manager_report.report()
        cache = live_data_cache_report_service.report()
        quality = self.quality_score()
        return {
            "ready": core["ready"] and stream["ready"] and cache["ready"] and quality["ready"],
            "core_ready": core["ready"],
            "stream_ready": stream["ready"],
            "cache_ready": cache["ready"],
            "quality_ready": quality["ready"],
            "quality_score": quality["overall"],
            "execution_allowed": False,
        }

live_data_enterprise_service = LiveDataEnterpriseService()
