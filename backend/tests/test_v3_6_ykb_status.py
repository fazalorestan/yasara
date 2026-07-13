from app.v36_phase_a_meta_ykb.service import PhaseAMetaYKBServiceV36

def test_v36_ykb_status():
    s = PhaseAMetaYKBServiceV36().ykb_status()
    assert s["ready"] is True
    assert "entries_count" in s
