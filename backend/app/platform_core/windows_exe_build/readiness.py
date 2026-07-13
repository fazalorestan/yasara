from app.platform_core.windows_exe_build.report import windows_exe_build_script_report_service

class WindowsExeBuildScriptReadinessGate:
    def run(self):
        r = windows_exe_build_script_report_service.report()
        ready = r["ready"] and r["dist_cleaner"]["safe"] and r["command_builder"]["ready"] and r["spec_validator"]["valid"] and r["dry_run_executor"]["return_code"] == 0 and r["artifact_plan"]["ready"] and r["dry_run"] is True and r["final_exe_generated"] is False
        return {"ready": ready, "checks": {"dist_cleaner_safe": r["dist_cleaner"]["safe"], "command_builder_ready": r["command_builder"]["ready"], "spec_valid": r["spec_validator"]["valid"], "dry_run_return_code": r["dry_run_executor"]["return_code"], "artifact_plan_ready": r["artifact_plan"]["ready"], "final_exe_generated": r["final_exe_generated"], "real_execution_enabled": r["real_execution_enabled"], "real_broker_connection_enabled": r["real_broker_connection_enabled"]}}
windows_exe_build_script_readiness_gate = WindowsExeBuildScriptReadinessGate()
