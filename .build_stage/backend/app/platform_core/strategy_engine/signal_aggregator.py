from app.platform_core.strategy_engine.confidence_model import strategy_confidence_model
from app.platform_core.strategy_engine.signal_evaluator import strategy_signal_evaluator
from app.platform_core.strategy_engine.strategy_score import strategy_score_service

class StrategySignalAggregator:
    def aggregate(self):
        signal = strategy_signal_evaluator.evaluate()
        score = strategy_score_service.score()
        confidence = strategy_confidence_model.confidence(score["score"])
        return {
            "ready": True,
            "signal": signal,
            "score": score,
            "confidence": confidence,
            "final_side": signal["side"],
            "execution_allowed": False,
        }

strategy_signal_aggregator = StrategySignalAggregator()
