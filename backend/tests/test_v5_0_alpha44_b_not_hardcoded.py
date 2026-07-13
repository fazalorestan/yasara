from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_not_hardcoded(): assert LiveDashboardFacadeV500Alpha44().contract()['hardcoded_dashboard'] is False
