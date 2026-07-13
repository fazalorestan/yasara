from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_facade_workspace():
 r=DesktopUIFacadeV500Alpha46().workspace(); assert r is not None
