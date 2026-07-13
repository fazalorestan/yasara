from app.v36_phase_a_meta_ykb.service import PhaseAMetaYKBServiceV36

def test_v36_health():
    h = PhaseAMetaYKBServiceV36().health_score()
    assert "overall_health_percent" in h
    assert h["live_trading_enabled"] is False
