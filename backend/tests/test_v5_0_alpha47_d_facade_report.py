from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_facade_report():
 r=BuildDashboardFacadeV500Alpha47().report(); assert r is not None
