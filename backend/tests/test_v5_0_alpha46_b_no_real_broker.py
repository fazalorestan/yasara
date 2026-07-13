from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_no_real_broker(): assert DesktopUIFacadeV500Alpha46().report()['real_broker_connection_enabled'] is False
