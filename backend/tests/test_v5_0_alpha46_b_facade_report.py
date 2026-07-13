from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_facade_report():
 r=DesktopUIFacadeV500Alpha46().report(); assert r is not None
