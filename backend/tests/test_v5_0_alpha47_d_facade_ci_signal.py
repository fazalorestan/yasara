from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_facade_ci_signal():
 r=BuildDashboardFacadeV500Alpha47().ci_signal(); assert r is not None
