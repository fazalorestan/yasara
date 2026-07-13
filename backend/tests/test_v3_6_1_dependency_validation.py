from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

def test_v361_dependency_validation():
    d = PhaseAGuardrailsServiceV361().dependency_validation()
    assert "checks" in d
    assert d["live_trading_enabled"] is False
