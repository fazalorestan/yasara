from app.v500_alpha44_desktop_dashboard.service import DesktopDashboardFacadeV500Alpha44

def test_not_hardcoded(): assert DesktopDashboardFacadeV500Alpha44().api_contract()['hardcoded_dashboard'] is False
