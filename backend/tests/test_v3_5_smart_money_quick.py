from app.v35_smart_money.service import SmartMoneyEngineServiceV35

def test_v35_quick():
    data = SmartMoneyEngineServiceV35().quick("BTCUSDT", "binance", "1m")
    assert data["symbol"] == "BTCUSDT"
    assert data["score"]["bias"] in ["bullish", "bearish", "neutral"]
