from app.platform_core.indicators.signal_logic.trend import TrendSignalLogic

def test_v500_alpha7_trend():
    r = TrendSignalLogic().evaluate({"ema_21": 10, "ema_55": 5})
    assert r["direction"] == "LONG"
