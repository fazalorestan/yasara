from app.v500_alpha46_desktop_ui.service import DesktopUIFacadeV500Alpha46

def test_facade_dashboard_connector():
 r=DesktopUIFacadeV500Alpha46().dashboard_connector(); assert r is not None
