from app.v11_ai_market_intelligence.models import MarketFeatureVectorV11, RiskLevelV11


class AIRiskClassifierV11:
    def classify(self, features: MarketFeatureVectorV11) -> RiskLevelV11:
        if features.volatility_score >= 0.7:
            return RiskLevelV11.HIGH
        if features.spread and features.last_price and (features.spread / features.last_price) > 0.001:
            return RiskLevelV11.MEDIUM
        return RiskLevelV11.LOW
