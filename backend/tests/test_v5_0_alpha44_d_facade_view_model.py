from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_facade_view_model():
 r=DesktopDashboardFacadeV500Alpha44().view_model(); assert r is not None
