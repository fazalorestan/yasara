from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_facade_notifications():
 r=DesktopUIFacadeV500Alpha46().notifications(); assert r is not None
