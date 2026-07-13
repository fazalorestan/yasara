from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_facade_build_timeline():
 r=BuildDashboardFacadeV500Alpha47().build_timeline(); assert r is not None
