from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_facade_sidebar():
 r=DesktopUIFacadeV500Alpha46().sidebar(); assert r is not None
