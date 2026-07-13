from app.v500_alpha40_ai_core.models import AICoreSummaryV500Alpha40

def test_v500_alpha40_a_summary():
 s=AICoreSummaryV500Alpha40(); assert s.ready and s.test_pack_size==60
