from app.platform_core.indicators.signal_logic.volatility import VolatilitySignalLogic

def test_v500_alpha7_volatility():
    r = VolatilitySignalLogic().evaluate({"atr_14": 2})
    assert r["risk"] == "active"
