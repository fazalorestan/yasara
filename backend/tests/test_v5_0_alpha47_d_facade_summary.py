from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_facade_summary():
 r=BuildDashboardFacadeV500Alpha47().summary(); assert r is not None
