from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_facade_status_bar():
 r=DesktopUIFacadeV500Alpha46().status_bar(); assert r is not None
