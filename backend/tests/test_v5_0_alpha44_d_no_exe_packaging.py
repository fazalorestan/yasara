from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_no_exe_packaging(): assert DesktopDashboardFacadeV500Alpha44().summary().exe_packaging_enabled is False
