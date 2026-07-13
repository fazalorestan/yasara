from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_facade_shell():
 assert DesktopDashboardGUIShellFacadeV500Alpha49().shell() is not None
