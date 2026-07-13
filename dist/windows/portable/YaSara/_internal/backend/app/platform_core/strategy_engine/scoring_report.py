from app.platform_core.strategy_engine.rule_evaluator import strategy_rule_evaluator
from app.platform_core.strategy_engine.scoring_safety import strategy_scoring_safety_policy
from app.platform_core.strategy_engine.signal_aggregator import strategy_signal_aggregator
from app.platform_core.strategy_engine.signal_evaluator import strategy_signal_evaluator
from app.platform_core.strategy_engine.strategy_score import strategy_score_service
from app.platform_core.strategy_engine.confidence_model import strategy_confidence_model

class StrategyScoringReport:
    def report(self):
        score = strategy_score_service.score()
        return {
            "ready": True,
            "signal_evaluation": strategy_signal_evaluator.evaluate(),
            "strategy_score": score,
            "confidence": strategy_confidence_model.confidence(score["score"]),
            "rules": strategy_rule_evaluator.evaluate(),
            "aggregation": strategy_signal_aggregator.aggregate(),
            "safety": strategy_scoring_safety_policy.policy(),
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

strategy_scoring_report = StrategyScoringReport()
