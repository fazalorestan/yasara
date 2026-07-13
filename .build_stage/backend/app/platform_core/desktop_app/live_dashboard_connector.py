from app.platform_core.project_intelligence.dashboard_report import live_dashboard_report_service

class DesktopLiveDashboardConnector:
    def connect(self):
        report = live_dashboard_report_service.report()
        return {
            "ready": True,
            "connected": True,
            "source": "live_dashboard_backend",
            "dashboard_backend_ready": report["ready"],
            "project_progress": report["progress"]["project_progress_percent"],
            "tests_passed": report["tests"]["passed"],
            "project_health": report["health"]["project_health"],
            "hardcoded_dashboard": False,
        }

desktop_live_dashboard_connector = DesktopLiveDashboardConnector()
