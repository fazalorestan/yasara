from app.platform_core.desktop_app.desktop_report import desktop_host_report_service
class DesktopHostReadinessGate:
    def run(self):
        r = desktop_host_report_service.report()
        ready = r["ready"] and r["host"]["ready"] and r["bootstrap"]["bootstrapped"] and r["window"]["main_window"] and r["navigation"]["dashboard_route_enabled"] and r["session"]["active"] and r["health"]["crash_detected"] is False and r["commercial_execution_engine_enabled"] is False
        return {"ready": ready, "checks": {"host_ready": r["host"]["ready"], "bootstrap_ready": r["bootstrap"]["bootstrapped"], "window_ready": r["window"]["main_window"], "dashboard_route_enabled": r["navigation"]["dashboard_route_enabled"], "session_active": r["session"]["active"], "crash_detected": r["health"]["crash_detected"], "commercial_execution_engine_enabled": False, "commercial_api_key_required": False, "real_execution_enabled": False, "real_broker_connection_enabled": False}}
desktop_host_readiness_gate = DesktopHostReadinessGate()
