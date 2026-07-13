from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_not_hardcoded(): assert BuildDashboardFacadeV500Alpha47().report()['hardcoded_dashboard'] is False
