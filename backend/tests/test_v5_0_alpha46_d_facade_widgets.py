from app.v500_alpha46_desktop_dashboard_intelligence.service import DesktopDashboardIntelligenceFacadeV500Alpha46

def test_facade_widgets():
 r=DesktopDashboardIntelligenceFacadeV500Alpha46().widgets(); assert r is not None
