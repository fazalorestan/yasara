from app.v500_alpha49_desktop_gui.service import DesktopDashboardGUIShellFacadeV500Alpha49

def test_no_real_broker(): assert DesktopDashboardGUIShellFacadeV500Alpha49().report()['real_broker_connection_enabled'] is False
