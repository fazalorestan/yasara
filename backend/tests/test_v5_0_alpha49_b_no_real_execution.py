from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_no_real_execution(): assert DesktopDashboardGUIShellFacadeV500Alpha49().report()['real_execution_enabled'] is False
