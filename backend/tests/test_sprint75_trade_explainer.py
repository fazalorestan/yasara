from app.ai_trading_v1.trade_explainer import TradeExplainerV1, TradeExplanationInputV1

def test_trade_explainer_summary():
    result = TradeExplainerV1().explain(TradeExplanationInputV1(symbol="BTC/USDT", direction="long", confidence=80, reasons=["trend up"]))
    assert "BTC/USDT" in result.title
    assert "trend up" in result.summary
