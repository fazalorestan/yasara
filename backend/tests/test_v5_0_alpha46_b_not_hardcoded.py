from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_not_hardcoded(): assert DesktopUIFacadeV500Alpha46().contract()['hardcoded_dashboard'] is False
