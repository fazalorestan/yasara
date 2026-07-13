from app.v500_alpha46_desktop_dashboard_intelligence.service import DesktopDashboardIntelligenceFacadeV500Alpha46

def test_facade_dashboard():
 r=DesktopDashboardIntelligenceFacadeV500Alpha46().dashboard(); assert r is not None
