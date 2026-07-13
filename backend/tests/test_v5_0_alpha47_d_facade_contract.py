from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_facade_contract():
 r=BuildDashboardFacadeV500Alpha47().contract(); assert r is not None
