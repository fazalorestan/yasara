from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_facade_ci_panel():
 assert DesktopDashboardGUIShellFacadeV500Alpha49().ci_panel() is not None
