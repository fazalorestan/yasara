from app.v500_alpha34_1_router_proof.models import RouterProofSummaryV500Alpha341

def test_v500_alpha34_1_summary():
 s=RouterProofSummaryV500Alpha341(); assert s.ready and s.manual_apply_required is False
