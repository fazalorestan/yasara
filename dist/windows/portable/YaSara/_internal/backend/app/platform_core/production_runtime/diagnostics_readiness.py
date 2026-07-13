from app.platform_core.production_runtime.diagnostics_report import runtime_diagnostics_report_service

class RuntimeDiagnosticsReadinessGate:
    def run(self):
        report = runtime_diagnostics_report_service.report()
        ready = report["ready"] and report["diagnostics"]["diagnostics_passed"] and report["stability"]["stable"] and report["crash_guard"]["crash_detected"] is False and report["resources"]["within_limits"] and report["commercial_execution_engine_enabled"] is False
        return {"ready": ready, "checks": {"diagnostics_passed": report["diagnostics"]["diagnostics_passed"], "stable": report["stability"]["stable"], "crash_detected": report["crash_guard"]["crash_detected"], "resources_within_limits": report["resources"]["within_limits"], "commercial_execution_engine_enabled": False, "commercial_api_key_required": False, "real_execution_enabled": False, "real_broker_connection_enabled": False}}
runtime_diagnostics_readiness_gate = RuntimeDiagnosticsReadinessGate()
