from app.v500_alpha50_release_candidate.models import InternalRCPreparationSummaryV500Alpha50

def test_summary():
 s=InternalRCPreparationSummaryV500Alpha50(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.50.E.001'
