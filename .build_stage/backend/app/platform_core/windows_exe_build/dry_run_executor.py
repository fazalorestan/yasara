from app.platform_core.windows_exe_build.command_builder import pyinstaller_command_builder
from app.platform_core.windows_exe_build.dist_cleaner import windows_dist_cleaner
from app.platform_core.windows_exe_build.spec_validator import windows_spec_validator

class WindowsExeDryRunBuildExecutor:
    def execute(self):
        return {"ready": True, "build_id": "2026.50.B.001", "dry_run": True, "cleaner": windows_dist_cleaner.plan(), "spec": windows_spec_validator.validate(), "command": pyinstaller_command_builder.command(), "return_code": 0, "final_exe_generated": False, "real_execution_enabled": False, "real_broker_connection_enabled": False}
windows_exe_dry_run_build_executor = WindowsExeDryRunBuildExecutor()
