from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_no_real_execution(): assert BuildDashboardFacadeV500Alpha47().report()['real_execution_enabled'] is False
