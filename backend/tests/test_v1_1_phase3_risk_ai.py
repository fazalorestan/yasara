from app.v11_ai_market_intelligence.models import MarketFeatureVectorV11, RiskLevelV11
from app.v11_ai_market_intelligence.risk_ai import AIRiskClassifierV11

def test_risk_ai_high_volatility():
    features = MarketFeatureVectorV11(symbol="BTCUSDT", last_price=1, volatility_score=0.8)
    assert AIRiskClassifierV11().classify(features) == RiskLevelV11.HIGH
