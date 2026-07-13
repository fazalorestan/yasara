from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_no_final_exe(): assert DesktopDashboardGUIShellFacadeV500Alpha49().summary().final_exe_generated is False
