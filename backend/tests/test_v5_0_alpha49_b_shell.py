from app.platform_core.desktop_gui.dashboard_shell import DesktopDashboardGUIShell

def test_shell(): assert DesktopDashboardGUIShell().shell()['hardcoded_dashboard_data'] is False
