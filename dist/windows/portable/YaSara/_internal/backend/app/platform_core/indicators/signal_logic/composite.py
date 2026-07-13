from app.platform_core.indicators.signal_logic.momentum import momentum_signal_logic
from app.platform_core.indicators.signal_logic.trend import trend_signal_logic
from app.platform_core.indicators.signal_logic.volatility import volatility_signal_logic

class CompositeSignalScorer:
    def score(self, math_output: dict):
        trend = trend_signal_logic.evaluate(math_output)
        momentum = momentum_signal_logic.evaluate(math_output)
        volatility = volatility_signal_logic.evaluate(math_output)
        total = min(100, trend["score"] + momentum["score"] + volatility["score"])
        return {
            "score": total,
            "parts": {
                "trend": trend,
                "momentum": momentum,
                "volatility": volatility,
            },
            "mode": "analysis_only",
        }

composite_signal_scorer = CompositeSignalScorer()
