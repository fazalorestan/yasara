from app.platform_core.windows_exe_build.artifact_plan import windows_exe_artifact_plan
from app.platform_core.windows_exe_build.build_log import windows_build_log_contract
from app.platform_core.windows_exe_build.command_builder import pyinstaller_command_builder
from app.platform_core.windows_exe_build.dist_cleaner import windows_dist_cleaner
from app.platform_core.windows_exe_build.dry_run_executor import windows_exe_dry_run_build_executor
from app.platform_core.windows_exe_build.readiness import windows_exe_build_script_readiness_gate
from app.platform_core.windows_exe_build.report import windows_exe_build_script_report_service
from app.platform_core.windows_exe_build.spec_validator import windows_spec_validator
from app.v500_alpha50_windows_exe_build.models import WindowsExeBuildScriptSummaryV500Alpha50

class WindowsExeBuildScriptFacadeV500Alpha50:
    def summary(self): return WindowsExeBuildScriptSummaryV500Alpha50()
    def dist_cleaner(self): return windows_dist_cleaner.plan()
    def command_builder(self): return pyinstaller_command_builder.command()
    def spec_validator(self): return windows_spec_validator.validate()
    def build_log(self): return windows_build_log_contract.log()
    def dry_run_executor(self): return windows_exe_dry_run_build_executor.execute()
    def artifact_plan(self): return windows_exe_artifact_plan.plan()
    def report(self): return windows_exe_build_script_report_service.report()
    def readiness(self): return windows_exe_build_script_readiness_gate.run()
    def contract(self): return {"ready": True, "windows_exe_build": "package_b_script_implementation", "build_id": "2026.50.B.001"}
windows_exe_build_script_facade_v500_alpha50 = WindowsExeBuildScriptFacadeV500Alpha50()
