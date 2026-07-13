from app.platform_core.windows_app.live_dashboard_host import WindowsLiveDashboardHost

def test_dashboard(): assert WindowsLiveDashboardHost().host()['hardcoded_dashboard'] is False
