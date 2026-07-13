from app.v11_ai_market_intelligence.models import MarketFeatureVectorV11, MarketRegimeV11, RegimeAnalysisV11, SignalDirectionV11
from app.v11_ai_market_intelligence.signal_scorer import SignalScorerV11

def test_signal_scorer_long():
    features = MarketFeatureVectorV11(symbol="BTCUSDT", last_price=50000, momentum_score=0.4)
    regime = RegimeAnalysisV11(symbol="BTCUSDT", regime=MarketRegimeV11.TRENDING_UP, confidence=0.7)
    signal = SignalScorerV11().score(features, regime)
    assert signal.direction == SignalDirectionV11.LONG
