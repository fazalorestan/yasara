from app.v500_alpha47_build_dashboard.models import BuildDashboardSummaryV500Alpha47

def test_summary():
 s=BuildDashboardSummaryV500Alpha47(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.47.D.001'
