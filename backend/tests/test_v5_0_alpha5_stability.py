from app.platform_core.indicators.release_gate.stability import IndicatorAlphaStabilityReport

def test_v500_alpha5_stability():
    r = IndicatorAlphaStabilityReport().report()
    assert r["ready"] is True
    assert r["stability"] == "green"
    assert r["live_execution_enabled"] is False
