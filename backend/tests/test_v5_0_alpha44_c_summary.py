from app.v500_alpha44_build_intelligence.models import BuildIntelligenceSummaryV500Alpha44

def test_summary():
 s=BuildIntelligenceSummaryV500Alpha44(); assert s.ready and s.test_pack_size==80 and s.hardcoded_dashboard is False
