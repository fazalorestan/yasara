from app.platform_core.desktop_app.build_information_provider import desktop_build_information_provider
from app.platform_core.desktop_app.dashboard_center import desktop_live_dashboard_center
from app.platform_core.desktop_app.dashboard_plugin_loader import desktop_dashboard_plugin_loader_contract
from app.platform_core.desktop_app.dashboard_widget_registry import desktop_dashboard_widget_registry
from app.platform_core.desktop_app.module_tracker import desktop_module_tracker
from app.platform_core.desktop_app.project_health_engine import desktop_project_health_engine
from app.platform_core.desktop_app.project_progress_engine import desktop_project_progress_engine
from app.platform_core.desktop_app.sprint_tracker import desktop_sprint_tracker
from app.platform_core.desktop_app.test_statistics_engine import desktop_test_statistics_engine

class DesktopDashboardIntelligenceReportService:
    def report(self):
        return {
            "ready": True,
            "dashboard": desktop_live_dashboard_center.dashboard(),
            "widgets": desktop_dashboard_widget_registry.widgets(),
            "plugin_loader": desktop_dashboard_plugin_loader_contract.contract(),
            "progress": desktop_project_progress_engine.progress(),
            "sprint": desktop_sprint_tracker.sprint(),
            "modules": desktop_module_tracker.modules(),
            "tests": desktop_test_statistics_engine.statistics(),
            "build": desktop_build_information_provider.build_info(),
            "health": desktop_project_health_engine.health(),
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

desktop_dashboard_intelligence_report_service = DesktopDashboardIntelligenceReportService()
DesktopDashboardIntelligenceReport = DesktopDashboardIntelligenceReportService
desktop_dashboard_intelligence_report = desktop_dashboard_intelligence_report_service
