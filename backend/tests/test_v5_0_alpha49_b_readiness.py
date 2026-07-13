from app.platform_core.desktop_gui.readiness import DesktopDashboardGUIShellReadinessGate

def test_readiness(): assert DesktopDashboardGUIShellReadinessGate().run()['ready'] is True
