from app.platform_core.indicators.release_gate.gate import IndicatorPlatform1000TestGate

def test_v500_alpha5_gate():
    g = IndicatorPlatform1000TestGate().run()
    assert g["ready"] is True
    assert g["score"] == 100.0
    assert g["execution_allowed"] is False
