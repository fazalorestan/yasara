from app.v36_phase_a_meta_ykb.service import PhaseAMetaYKBServiceV36

def test_v36_summary():
    s = PhaseAMetaYKBServiceV36().summary()
    assert s.product_progress_percent == 80
    assert s.constitution_compliant is True
