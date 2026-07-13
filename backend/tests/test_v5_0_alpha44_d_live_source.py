from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_live_source(): assert DesktopDashboardFacadeV500Alpha44().view_model()['source']=='live_dashboard_backend'
