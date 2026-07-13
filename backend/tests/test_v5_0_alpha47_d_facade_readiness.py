from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_facade_readiness():
 r=BuildDashboardFacadeV500Alpha47().readiness(); assert r is not None
