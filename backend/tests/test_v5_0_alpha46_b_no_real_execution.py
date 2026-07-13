from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_no_real_execution(): assert DesktopUIFacadeV500Alpha46().report()['real_execution_enabled'] is False
