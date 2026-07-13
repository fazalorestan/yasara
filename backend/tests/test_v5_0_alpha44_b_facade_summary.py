from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_facade_summary():
 r=LiveDashboardFacadeV500Alpha44().summary(); assert r is not None
