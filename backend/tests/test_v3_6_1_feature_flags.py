from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

def test_v361_feature_flags():
    f = PhaseAGuardrailsServiceV361().feature_flags_status()
    assert f["ready"] is True
    assert f["commercial_execution_excluded"] is True
