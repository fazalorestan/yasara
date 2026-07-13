from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_facade_sprint():
 r=LiveDashboardFacadeV500Alpha44().sprint(); assert r is not None
