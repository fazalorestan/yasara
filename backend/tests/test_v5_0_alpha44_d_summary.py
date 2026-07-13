from app.v500_alpha44_desktop_dashboard.models import DesktopDashboardSummaryV500Alpha44

def test_summary():
 s=DesktopDashboardSummaryV500Alpha44(); assert s.ready and s.test_pack_size==80 and s.hardcoded_dashboard is False
