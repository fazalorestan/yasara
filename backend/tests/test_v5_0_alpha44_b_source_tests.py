from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_source_tests(): assert LiveDashboardFacadeV500Alpha44().data()['tests']['ready'] is True
