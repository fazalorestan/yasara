from app.v500_alpha44_live_dashboard.service import LiveDashboardFacadeV500Alpha44

def test_facade_data():
 r=LiveDashboardFacadeV500Alpha44().data(); assert r is not None
