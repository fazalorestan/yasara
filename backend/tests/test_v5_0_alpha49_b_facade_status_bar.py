from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_facade_status_bar():
 assert DesktopDashboardGUIShellFacadeV500Alpha49().status_bar() is not None
