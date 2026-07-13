from app.platform_core.indicators.signal_logic.service import YaSaraRuntimeSignalLogicService

def test_v500_alpha7_service():
    r = YaSaraRuntimeSignalLogicService().evaluate({"ema_21": 10, "ema_55": 5, "rsi_14": 60, "macd": {"histogram": 1}, "atr_14": 2})
    assert r["ready"] is True
    assert r["execution_allowed"] is False
