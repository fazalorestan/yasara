from app.v41_indicator_engine.service import ModularIndicatorEngineServiceV41

def test_v41_quick():
    data = ModularIndicatorEngineServiceV41().quick()
    assert data["symbol"] == "BTCUSDT"
    assert data["aggregate"]["bias"] in ["bullish", "bearish", "neutral"]
