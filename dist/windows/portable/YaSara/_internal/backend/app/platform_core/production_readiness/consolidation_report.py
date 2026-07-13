from app.platform_core.build_pipeline.report import build_pipeline_report_service
from app.platform_core.ci_pipeline.report import ci_pipeline_report_service
from app.platform_core.release_registry.report import artifact_release_report_service
from app.platform_core.build_dashboard.report import build_dashboard_integration_report_service

class BuildCIReleaseConsolidationReportService:
    def report(self):
        return {
            "ready": True,
            "build_pipeline": build_pipeline_report_service.report(),
            "ci_pipeline": ci_pipeline_report_service.report(),
            "artifact_release": artifact_release_report_service.report(),
            "build_dashboard": build_dashboard_integration_report_service.report(),
            "consolidated": True,
            "packaging_enabled": False,
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

build_ci_release_consolidation_report_service = BuildCIReleaseConsolidationReportService()
