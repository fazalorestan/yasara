from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_facade_readiness():
 r=LiveDashboardFacadeV500Alpha44().readiness(); assert r is not None
