from app.v33_strategy_builder.service import StrategyBuilderServiceV33

def test_v33_demo_evaluate():
    service = StrategyBuilderServiceV33()
    service.demo_strategy()
    result = service.evaluate("demo-ema-rsi")
    assert result["ready"] is True
    assert result["action"] in ["buy", "sell", "hold", "block"]
    assert result["live_trading_enabled"] is False
