from app.platform_core.ci_pipeline.ci_core import ci_pipeline_core_service
from app.platform_core.ci_pipeline.ci_dashboard_provider import ci_dashboard_provider
from app.platform_core.ci_pipeline.test_report import ci_test_report_service

class CIPipelineReportService:
    def report(self):
        return {
            "ready": True,
            "core": ci_pipeline_core_service.status(),
            "test_report": ci_test_report_service.report(),
            "dashboard": ci_dashboard_provider.dashboard(),
            "external_ci_provider_enabled": False,
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

ci_pipeline_report_service = CIPipelineReportService()
CIPipelineReport = CIPipelineReportService
ci_pipeline_report = ci_pipeline_report_service
