from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_no_real_broker(): assert LiveDashboardFacadeV500Alpha44().health()['real_broker_connection_enabled'] is False
