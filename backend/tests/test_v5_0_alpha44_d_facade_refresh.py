from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_facade_refresh():
 r=DesktopDashboardFacadeV500Alpha44().refresh(); assert r is not None
