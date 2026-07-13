from app.platform_core.windows_portable_build.report import windows_portable_build_report_service

class WindowsPortableBuildReadinessGate:
    def run(self):
        r = windows_portable_build_report_service.report()
        ready = r["ready"] and r["layout"]["ready"] and r["manifest"]["ready"] and r["build_script"]["ready"] and r["build_script"]["does_not_enable_real_execution"] and r["artifact_registration"]["requires_hash"] and r["launch_smoke"]["ready"] and r["final_exe_generated"] is False
        return {"ready": ready, "checks": {"layout_ready": r["layout"]["ready"], "manifest_ready": r["manifest"]["ready"], "build_script_ready": r["build_script"]["ready"], "real_execution_disabled": r["real_execution_enabled"] is False, "broker_disabled": r["real_broker_connection_enabled"] is False, "requires_hash": r["artifact_registration"]["requires_hash"], "launch_smoke_ready": r["launch_smoke"]["ready"], "final_exe_generated": r["final_exe_generated"]}}

windows_portable_build_readiness_gate = WindowsPortableBuildReadinessGate()
