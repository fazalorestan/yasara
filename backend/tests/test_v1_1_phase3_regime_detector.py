from app.v11_ai_market_intelligence.models import MarketFeatureVectorV11, MarketRegimeV11
from app.v11_ai_market_intelligence.regime_detector import MarketRegimeDetectorV11

def test_regime_detector_trending_up():
    features = MarketFeatureVectorV11(symbol="BTCUSDT", last_price=50000, momentum_score=0.5)
    result = MarketRegimeDetectorV11().analyze(features)
    assert result.regime == MarketRegimeV11.TRENDING_UP
