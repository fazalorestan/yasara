from app.platform_core.windows_portable_build.dashboard_provider import WindowsPortableBuildDashboardProvider

def test_dashboard(): assert WindowsPortableBuildDashboardProvider().dashboard()['hardcoded_dashboard'] is False
