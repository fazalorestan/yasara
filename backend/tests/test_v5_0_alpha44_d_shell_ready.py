from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_shell_ready(): assert DesktopDashboardFacadeV500Alpha44().summary().desktop_shell_ready is True
