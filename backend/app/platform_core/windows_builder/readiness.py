from app.platform_core.windows_builder.report import windows_executable_builder_report_service
class WindowsExecutableBuilderReadinessGate:
    def run(self):
        r = windows_executable_builder_report_service.report()
        ready = r["ready"] and r["coordinator"]["ready"] and r["exe_contract"]["ready"] and r["portable"]["ready"] and r["installer"]["ready"] and r["startup"]["startup_valid"] and r["dependencies"]["dependencies_valid"] and r["smoke_test"]["smoke_test_passed"] and r["final_exe_generated"] is False
        return {"ready": ready, "checks": {"coordinator_ready": r["coordinator"]["ready"], "exe_contract_ready": r["exe_contract"]["ready"], "portable_ready": r["portable"]["ready"], "installer_ready": r["installer"]["ready"], "startup_valid": r["startup"]["startup_valid"], "dependencies_valid": r["dependencies"]["dependencies_valid"], "smoke_test_passed": r["smoke_test"]["smoke_test_passed"], "final_exe_generated": r["final_exe_generated"], "exe_packaging_enabled": r["exe_packaging_enabled"], "real_execution_enabled": False, "real_broker_connection_enabled": False}}
windows_executable_builder_readiness_gate = WindowsExecutableBuilderReadinessGate()
