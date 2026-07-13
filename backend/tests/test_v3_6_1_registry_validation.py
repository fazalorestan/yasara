from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

def test_v361_registry_validation():
    r = PhaseAGuardrailsServiceV361().registry_validation()
    assert "features_count" in r
    assert r["live_trading_enabled"] is False
