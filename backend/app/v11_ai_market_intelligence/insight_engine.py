from app.v11_ai_market_intelligence.feature_builder import MarketFeatureBuilderV11
from app.v11_ai_market_intelligence.models import AIMarketInsightV11
from app.v11_ai_market_intelligence.regime_detector import MarketRegimeDetectorV11
from app.v11_ai_market_intelligence.signal_scorer import SignalScorerV11
from app.v11_market_data.models import MarketSnapshotItemV11


class AIMarketInsightEngineV11:
    def __init__(self):
        self.features = MarketFeatureBuilderV11()
        self.regime = MarketRegimeDetectorV11()
        self.scorer = SignalScorerV11()

    def analyze_item(self, item: MarketSnapshotItemV11) -> AIMarketInsightV11:
        feature_vector = self.features.from_snapshot_item(item)
        regime = self.regime.analyze(feature_vector)
        signal = self.scorer.score(feature_vector, regime)
        warnings: list[str] = []
        if signal.risk_level.value == "high":
            warnings.append("risk_guard_active")
        return AIMarketInsightV11(
            ready=True,
            symbol=feature_vector.symbol,
            regime=regime,
            signal=signal,
            warnings=warnings,
        )
