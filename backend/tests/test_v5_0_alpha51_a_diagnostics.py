from app.platform_core.windows_exe_smoke_build.failure_diagnostics import WindowsExeBuildFailureDiagnostics

def test_diagnostics(): assert WindowsExeBuildFailureDiagnostics().diagnostics()['dashboard_visible'] is True
