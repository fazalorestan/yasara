from app.platform_core.indicators.signal_adapter import YaSaraSignalAdapter

def test_v441_signal_adapter():
    s = YaSaraSignalAdapter().normalize({"direction": "LONG", "score": 120})
    assert s["indicator"] == "yasara"
    assert s["confidence"] == 100
    assert s["execution_allowed"] is False
