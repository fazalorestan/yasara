from app.v52_alpha_baseline_syntax_recovery.models import BaselineSyntaxRecoverySummaryV52Alpha

def test_summary():
    s = BaselineSyntaxRecoverySummaryV52Alpha()
    assert s.ready
    assert s.build_id == "2026.52.Q.001"
    assert s.test_pack_size == 90
