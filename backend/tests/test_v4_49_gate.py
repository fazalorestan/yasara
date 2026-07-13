from app.platform_core.indicators.readiness.gate import YaSaraIndicatorReadinessGate

def test_v449_gate():
    g = YaSaraIndicatorReadinessGate().run()
    assert g["ready"] is True
    assert g["score"] == 100.0
    assert g["execution_allowed"] is False
