from app.platform_core.project_intelligence.dashboard_report import live_dashboard_report_service
class LiveDashboardReadinessGate:
    def run(self):
        r = live_dashboard_report_service.report()
        ready = r["ready"] and r["data"]["ready"] and r["progress"]["ready"] and r["tests"]["ready"] and r["modules"]["ready"] and r["health"]["ready"] and r["hardcoded_dashboard"] is False
        return {"ready": ready, "checks": {"data_provider_ready": r["data"]["ready"], "progress_ready": r["progress"]["ready"], "tests_ready": r["tests"]["ready"], "modules_ready": r["modules"]["ready"], "health_ready": r["health"]["ready"], "hardcoded_dashboard": False}}
live_dashboard_readiness_gate = LiveDashboardReadinessGate()
