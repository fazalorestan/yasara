from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_facade_layout():
 r=DesktopUIFacadeV500Alpha46().layout(); assert r is not None
