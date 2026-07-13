from app.platform_core.project_intelligence.dashboard_report import live_dashboard_report_service

class DashboardViewModelService:
    def view_model(self):
        report = live_dashboard_report_service.report()
        return {
            "ready": True,
            "title": "YaSara Project Dashboard",
            "project_progress": report["progress"]["project_progress_percent"],
            "platform_progress": report["platform_progress"]["platforms"],
            "tests": report["tests"],
            "modules": report["modules"],
            "sprint": report["sprint"],
            "health": report["health"],
            "source": "live_dashboard_backend",
            "hardcoded_dashboard": False,
        }

dashboard_view_model_service = DashboardViewModelService()
