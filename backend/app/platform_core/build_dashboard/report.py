from app.platform_core.build_dashboard.artifact_signal_provider import artifact_signal_provider
from app.platform_core.build_dashboard.build_timeline_provider import build_timeline_provider
from app.platform_core.build_dashboard.ci_signal_provider import ci_signal_provider
from app.platform_core.build_dashboard.integration_center import build_dashboard_integration_center
from app.platform_core.build_dashboard.pipeline_status_provider import pipeline_status_provider
from app.platform_core.build_dashboard.quality_signal_provider import build_quality_signal_provider
from app.platform_core.build_dashboard.release_signal_provider import release_signal_provider

class BuildDashboardIntegrationReportService:
    def report(self):
        return {
            "ready": True,
            "integration": build_dashboard_integration_center.dashboard(),
            "pipeline_status": pipeline_status_provider.status(),
            "build_timeline": build_timeline_provider.timeline(),
            "ci_signal": ci_signal_provider.signal(),
            "release_signal": release_signal_provider.signal(),
            "artifact_signal": artifact_signal_provider.signal(),
            "quality_signal": build_quality_signal_provider.signal(),
            "build_id": "2026.47.D.001",
            "packaging_enabled": False,
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

build_dashboard_integration_report_service = BuildDashboardIntegrationReportService()
BuildDashboardIntegrationReport = BuildDashboardIntegrationReportService
build_dashboard_integration_report = build_dashboard_integration_report_service
