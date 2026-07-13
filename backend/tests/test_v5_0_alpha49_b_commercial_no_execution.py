from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_commercial_no_execution(): assert DesktopDashboardGUIShellFacadeV500Alpha49().report()['commercial_execution_engine_enabled'] is False
