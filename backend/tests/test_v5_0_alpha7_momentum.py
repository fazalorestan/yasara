from app.platform_core.indicators.signal_logic.momentum import MomentumSignalLogic

def test_v500_alpha7_momentum():
    r = MomentumSignalLogic().evaluate({"rsi_14": 60, "macd": {"histogram": 1}})
    assert r["score"] >= 15
