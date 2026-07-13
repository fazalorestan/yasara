from app.platform_core.windows_exe_build.artifact_plan import windows_exe_artifact_plan
from app.platform_core.windows_exe_build.build_log import windows_build_log_contract
from app.platform_core.windows_exe_build.command_builder import pyinstaller_command_builder
from app.platform_core.windows_exe_build.dist_cleaner import windows_dist_cleaner
from app.platform_core.windows_exe_build.dry_run_executor import windows_exe_dry_run_build_executor
from app.platform_core.windows_exe_build.spec_validator import windows_spec_validator

class WindowsExeBuildScriptReportService:
    def report(self):
        return {"ready": True, "build_id": "2026.50.B.001", "dist_cleaner": windows_dist_cleaner.plan(), "command_builder": pyinstaller_command_builder.command(), "spec_validator": windows_spec_validator.validate(), "build_log": windows_build_log_contract.log(), "dry_run_executor": windows_exe_dry_run_build_executor.execute(), "artifact_plan": windows_exe_artifact_plan.plan(), "final_exe_generated": False, "dry_run": True, "real_execution_enabled": False, "real_broker_connection_enabled": False, "commercial_execution_engine_enabled": False, "commercial_api_key_required": False}
windows_exe_build_script_report_service = WindowsExeBuildScriptReportService()
WindowsExeBuildScriptReport = WindowsExeBuildScriptReportService
windows_exe_build_script_report = windows_exe_build_script_report_service
