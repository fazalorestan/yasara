from app.market_tools_v1.liquidity import LiquidityInputV1, LiquidityScoreEngineV1

def test_liquidity_score_high():
    result = LiquidityScoreEngineV1().score(LiquidityInputV1(volume=2000, spread_percent=0.1))
    assert result.level == "high"
