from app.platform_core.windows_real_exe.report import windows_real_exe_build_pipeline_report_service

class WindowsRealExeBuildPipelineReadinessGate:
    def run(self):
        r = windows_real_exe_build_pipeline_report_service.report()
        ready = (
            r["ready"]
            and r["pyinstaller"]["ready"]
            and r["spec"]["ready"]
            and r["portable_builder"]["ready"]
            and r["build_script"]["requires_pyinstaller"]
            and r["artifact_hash"]["hash_required"]
            and r["real_execution_enabled"] is False
            and r["real_broker_connection_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "pyinstaller_contract_ready": r["pyinstaller"]["ready"],
                "spec_ready": r["spec"]["ready"],
                "portable_builder_ready": r["portable_builder"]["ready"],
                "build_script_ready": r["build_script"]["ready"],
                "artifact_hash_required": r["artifact_hash"]["hash_required"],
                "final_exe_generated": r["final_exe_generated"],
                "real_execution_enabled": r["real_execution_enabled"],
                "real_broker_connection_enabled": r["real_broker_connection_enabled"],
            },
        }
windows_real_exe_build_pipeline_readiness_gate = WindowsRealExeBuildPipelineReadinessGate()
