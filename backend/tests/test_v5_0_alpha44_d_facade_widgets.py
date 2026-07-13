from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_facade_widgets():
 r=DesktopDashboardFacadeV500Alpha44().widgets(); assert r is not None
