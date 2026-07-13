from app.v500_alpha44_live_dashboard.models import LiveDashboardSummaryV500Alpha44

def test_summary():
 s=LiveDashboardSummaryV500Alpha44(); assert s.ready and s.test_pack_size==80 and s.hardcoded_dashboard is False
