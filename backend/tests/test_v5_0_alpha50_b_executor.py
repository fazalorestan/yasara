from app.platform_core.windows_exe_build.dry_run_executor import WindowsExeDryRunBuildExecutor

def test_executor(): assert WindowsExeDryRunBuildExecutor().execute()['return_code'] == 0
