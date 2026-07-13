from app.platform_core.project_intelligence.pic_report import project_intelligence_report_service
class DashboardDataProvider:
    def data(self):
        r = project_intelligence_report_service.report()
        return {"ready": True, "source": "pic_registries", "hardcoded_dashboard": False, "project": r["project"], "sprint": r["sprint"], "version": r["version"], "build": r["build"], "tests": r["tests"], "modules": r["modules"], "health": r["health"]}
dashboard_data_provider = DashboardDataProvider()
