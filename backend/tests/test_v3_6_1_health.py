from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

def test_v361_health():
    h = PhaseAGuardrailsServiceV361().health_aggregate()
    assert "overall_health_percent" in h
    assert h["live_trading_enabled"] is False
