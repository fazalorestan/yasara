from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_widgets_count(): assert DesktopDashboardFacadeV500Alpha44().widgets()['count']==8
