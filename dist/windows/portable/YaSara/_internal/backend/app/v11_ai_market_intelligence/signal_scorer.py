from app.v11_ai_market_intelligence.models import (
    MarketFeatureVectorV11,
    MarketRegimeV11,
    RegimeAnalysisV11,
    RiskLevelV11,
    SignalDirectionV11,
    SignalScoreV11,
)
from app.v11_ai_market_intelligence.risk_ai import AIRiskClassifierV11


class SignalScorerV11:
    def __init__(self):
        self.risk = AIRiskClassifierV11()

    def score(self, features: MarketFeatureVectorV11, regime: RegimeAnalysisV11) -> SignalScoreV11:
        risk_level = self.risk.classify(features)
        if risk_level == RiskLevelV11.HIGH:
            return SignalScoreV11(
                symbol=features.symbol,
                direction=SignalDirectionV11.NEUTRAL,
                score=0.0,
                confidence=0.5,
                risk_level=risk_level,
                explanation="High volatility detected; signal suppressed by risk guard.",
            )
        if regime.regime == MarketRegimeV11.TRENDING_UP:
            score = min(0.5 + features.momentum_score, 1.0)
            return SignalScoreV11(
                symbol=features.symbol,
                direction=SignalDirectionV11.LONG,
                score=score,
                confidence=regime.confidence,
                risk_level=risk_level,
                explanation="Momentum and regime suggest a long-biased read-only signal.",
            )
        if regime.regime == MarketRegimeV11.TRENDING_DOWN:
            return SignalScoreV11(
                symbol=features.symbol,
                direction=SignalDirectionV11.SHORT,
                score=0.6,
                confidence=regime.confidence,
                risk_level=risk_level,
                explanation="Regime suggests a short-biased read-only signal.",
            )
        return SignalScoreV11(
            symbol=features.symbol,
            direction=SignalDirectionV11.NEUTRAL,
            score=0.2,
            confidence=regime.confidence,
            risk_level=risk_level,
            explanation="Market appears range-bound or inconclusive.",
        )
