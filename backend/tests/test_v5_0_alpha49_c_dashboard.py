from app.platform_core.desktop_launcher.dashboard_launch_contract import DashboardLaunchContract

def test_dashboard(): assert DashboardLaunchContract().contract()['hardcoded_dashboard_data'] is False
