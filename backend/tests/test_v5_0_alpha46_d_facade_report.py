from app.v500_alpha46_desktop_dashboard_intelligence.service import DesktopDashboardIntelligenceFacadeV500Alpha46

def test_facade_report():
 r=DesktopDashboardIntelligenceFacadeV500Alpha46().report(); assert r is not None
