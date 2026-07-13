from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_facade_ui_state():
 assert DesktopDashboardGUIShellFacadeV500Alpha49().ui_state() is not None
