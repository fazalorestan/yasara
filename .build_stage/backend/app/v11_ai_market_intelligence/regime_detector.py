from app.v11_ai_market_intelligence.models import MarketFeatureVectorV11, MarketRegimeV11, RegimeAnalysisV11


class MarketRegimeDetectorV11:
    def analyze(self, features: MarketFeatureVectorV11) -> RegimeAnalysisV11:
        reasons: list[str] = []
        if features.volatility_score >= 0.7:
            reasons.append("wide_spread_or_high_volatility")
            return RegimeAnalysisV11(symbol=features.symbol, regime=MarketRegimeV11.VOLATILE, confidence=0.75, reasons=reasons)
        if features.momentum_score >= 0.3 and (features.funding_rate or 0) >= 0:
            reasons.append("positive_momentum")
            return RegimeAnalysisV11(symbol=features.symbol, regime=MarketRegimeV11.TRENDING_UP, confidence=0.65, reasons=reasons)
        if features.momentum_score <= -0.3:
            reasons.append("negative_momentum")
            return RegimeAnalysisV11(symbol=features.symbol, regime=MarketRegimeV11.TRENDING_DOWN, confidence=0.65, reasons=reasons)
        reasons.append("low_directional_signal")
        return RegimeAnalysisV11(symbol=features.symbol, regime=MarketRegimeV11.RANGING, confidence=0.55, reasons=reasons)
