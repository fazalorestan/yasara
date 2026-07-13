from app.ai_trading_v1.market_context import MarketContextAIV1, MarketContextInputV1

def test_market_context_caution():
    result = MarketContextAIV1().classify(MarketContextInputV1(regime="trending_up", volatility_level="high", liquidity_level="medium"))
    assert result.caution is True
