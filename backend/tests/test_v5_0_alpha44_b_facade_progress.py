from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_facade_progress():
 r=LiveDashboardFacadeV500Alpha44().progress(); assert r is not None
