from app.platform_core.indicators.readiness.e2e_contract import YaSaraIndicatorE2EContract

def test_v449_e2e_contract():
    c = YaSaraIndicatorE2EContract().contract()
    assert c["ready"] is True
    assert "runtime_adapter" in c["pipeline"]
    assert c["execution_allowed"] is False
