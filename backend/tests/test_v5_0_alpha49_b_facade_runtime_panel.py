from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_facade_runtime_panel():
 assert DesktopDashboardGUIShellFacadeV500Alpha49().runtime_panel() is not None
