from app.v33_strategy_builder.service import StrategyBuilderServiceV33

def test_v33_context():
    data = StrategyBuilderServiceV33().build_context_from_ai("BTCUSDT", "binance", "1m")
    assert data["symbol"] == "BTCUSDT"
    assert "ai_score" in data["fields"]
    assert data["live_trading_enabled"] is False
