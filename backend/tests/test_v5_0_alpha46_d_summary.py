from app.v500_alpha46_desktop_dashboard_intelligence.models import DesktopDashboardIntelligenceSummaryV500Alpha46

def test_summary():
 s=DesktopDashboardIntelligenceSummaryV500Alpha46(); assert s.ready and s.test_pack_size==80 and s.hardcoded_dashboard is False
