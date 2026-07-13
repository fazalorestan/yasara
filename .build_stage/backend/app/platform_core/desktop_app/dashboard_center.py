from app.platform_core.project_intelligence.dashboard_report import live_dashboard_report_service

class DesktopLiveDashboardCenter:
    def dashboard(self):
        report = live_dashboard_report_service.report()
        return {
            "ready": True,
            "source": "live_dashboard_backend",
            "project_progress": report["progress"]["project_progress_percent"],
            "platform_progress": report["platform_progress"]["platforms"],
            "tests": report["tests"],
            "modules": report["modules"],
            "sprint": report["sprint"],
            "health": report["health"],
            "hardcoded_dashboard": False,
        }

desktop_live_dashboard_center = DesktopLiveDashboardCenter()
