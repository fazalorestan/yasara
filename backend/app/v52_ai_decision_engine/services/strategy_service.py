from app.v52_ai_decision_engine.models import DecisionResult

class StrategyService:
    def align(self, result: DecisionResult):
        c = result.confidence
        return {
            "scalp": round(c * .75, 4),
            "day_trade": round(c * .85, 4),
            "swing": round(c * .95, 4),
            "trend": round(c, 4),
            "mean_reversion": round(max(0.0, 1.0 - c), 4),
            "momentum": round(c * .90, 4),
            "breakout": round(c * .88, 4),
        }
