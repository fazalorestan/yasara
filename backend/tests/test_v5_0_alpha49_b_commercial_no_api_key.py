from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_commercial_no_api_key(): assert DesktopDashboardGUIShellFacadeV500Alpha49().report()['commercial_api_key_required'] is False
