from app.platform_core.project_intelligence.dashboard_data_provider import dashboard_data_provider
from app.platform_core.project_intelligence.health_summary_view import health_summary_view_service
from app.platform_core.project_intelligence.module_summary_view import module_summary_view_service
from app.platform_core.project_intelligence.platform_progress_view import platform_progress_view_service
from app.platform_core.project_intelligence.progress_calculator import project_progress_calculator
from app.platform_core.project_intelligence.sprint_summary_view import sprint_summary_view_service
from app.platform_core.project_intelligence.test_summary_view import test_summary_view_service
class LiveDashboardReportService:
    def report(self):
        return {"ready": True, "data": dashboard_data_provider.data(), "progress": project_progress_calculator.progress(), "platform_progress": platform_progress_view_service.view(), "tests": test_summary_view_service.view(), "modules": module_summary_view_service.view(), "sprint": sprint_summary_view_service.view(), "health": health_summary_view_service.view(), "hardcoded_dashboard": False, "dashboard_backend": "live"}
live_dashboard_report_service = LiveDashboardReportService()
LiveDashboardReport = LiveDashboardReportService
live_dashboard_report = live_dashboard_report_service
