from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_no_real_execution(): assert LiveDashboardFacadeV500Alpha44().health()['real_execution_enabled'] is False
