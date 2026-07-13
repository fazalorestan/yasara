from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_commercial_no_execution(): assert BuildDashboardFacadeV500Alpha47().report()['commercial_execution_engine_enabled'] is False
