from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

def test_v361_summary():
    s = PhaseAGuardrailsServiceV361().summary()
    assert s.product_progress_percent == 82
    assert s.constitution_compliant is True
