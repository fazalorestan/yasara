from app.platform_core.desktop_app.foundation_report import desktop_foundation_report_service
class DesktopFoundationReadinessGate:
    def run(self):
        r = desktop_foundation_report_service.report()
        ready = r["ready"] and r["host"]["ready"] and r["stabilization"]["ready"] and r["ui"]["ready"] and r["workspace"]["ready"] and r["dashboard_intelligence"]["ready"] and r["dashboard_validation"]["validated"] and r["quality"]["ready"] and r["acceptance"]["ready"] and r["hardcoded_dashboard"] is False and r["commercial_execution_engine_enabled"] is False
        return {"ready": ready, "checks": {"host_ready": r["host"]["ready"], "stabilization_ready": r["stabilization"]["ready"], "ui_ready": r["ui"]["ready"], "workspace_ready": r["workspace"]["ready"], "dashboard_intelligence_ready": r["dashboard_intelligence"]["ready"], "dashboard_validated": r["dashboard_validation"]["validated"], "quality_ready": r["quality"]["ready"], "acceptance_ready": r["acceptance"]["ready"], "exe_packaging_enabled": r["exe_packaging_enabled"], "hardcoded_dashboard": False, "commercial_execution_engine_enabled": False, "commercial_api_key_required": False, "real_execution_enabled": False, "real_broker_connection_enabled": False}}
desktop_foundation_readiness_gate = DesktopFoundationReadinessGate()
