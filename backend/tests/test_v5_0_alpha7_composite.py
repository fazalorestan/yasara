from app.platform_core.indicators.signal_logic.composite import CompositeSignalScorer

def test_v500_alpha7_composite():
    r = CompositeSignalScorer().score({"ema_21": 10, "ema_55": 5, "rsi_14": 60, "macd": {"histogram": 1}, "atr_14": 2})
    assert r["score"] > 0
