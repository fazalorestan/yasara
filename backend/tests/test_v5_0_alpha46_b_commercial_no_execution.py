from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_commercial_no_execution(): assert DesktopUIFacadeV500Alpha46().report()['commercial_execution_engine_enabled'] is False
