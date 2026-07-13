from app.platform_core.windows_real_exe.artifact_hash import windows_exe_artifact_hash_contract
from app.platform_core.windows_real_exe.build_script import windows_real_exe_build_script_contract
from app.platform_core.windows_real_exe.portable_builder import windows_real_portable_builder
from app.platform_core.windows_real_exe.pyinstaller_contract import windows_pyinstaller_contract
from app.platform_core.windows_real_exe.smoke_test import windows_real_exe_smoke_test_contract
from app.platform_core.windows_real_exe.spec_contract import windows_exe_spec_contract

class WindowsRealExeBuildPipelineReportService:
    def report(self):
        return {
            "ready": True,
            "build_id": "2026.50.A.001",
            "pyinstaller": windows_pyinstaller_contract.contract(),
            "spec": windows_exe_spec_contract.spec(),
            "portable_builder": windows_real_portable_builder.builder(),
            "build_script": windows_real_exe_build_script_contract.contract(),
            "artifact_hash": windows_exe_artifact_hash_contract.hash_contract(),
            "smoke_test": windows_real_exe_smoke_test_contract.smoke(),
            "final_exe_generated": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }
windows_real_exe_build_pipeline_report_service = WindowsRealExeBuildPipelineReportService()
WindowsRealExeBuildPipelineReport = WindowsRealExeBuildPipelineReportService
windows_real_exe_build_pipeline_report = windows_real_exe_build_pipeline_report_service
