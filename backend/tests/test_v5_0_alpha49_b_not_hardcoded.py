from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_not_hardcoded(): assert DesktopDashboardGUIShellFacadeV500Alpha49().summary().hardcoded_dashboard_data is False
