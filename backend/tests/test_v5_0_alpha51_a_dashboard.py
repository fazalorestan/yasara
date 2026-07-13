from app.platform_core.windows_exe_smoke_build.dashboard_status import WindowsExeSmokeDashboardStatus

def test_dashboard(): assert WindowsExeSmokeDashboardStatus().status()['hardcoded_dashboard'] is False
