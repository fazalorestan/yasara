from app.market_tools_v1.regime import MarketRegime, MarketRegimeDetectorV1

def test_market_regime_trending_up():
    result = MarketRegimeDetectorV1().detect([100, 103])
    assert result.regime == MarketRegime.TRENDING_UP
