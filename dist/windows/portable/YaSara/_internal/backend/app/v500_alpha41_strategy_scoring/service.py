from app.platform_core.strategy_engine.confidence_model import strategy_confidence_model
from app.platform_core.strategy_engine.rule_evaluator import strategy_rule_evaluator
from app.platform_core.strategy_engine.scoring_readiness import strategy_scoring_readiness_gate
from app.platform_core.strategy_engine.scoring_report import strategy_scoring_report
from app.platform_core.strategy_engine.scoring_safety import strategy_scoring_safety_policy
from app.platform_core.strategy_engine.signal_aggregator import strategy_signal_aggregator
from app.platform_core.strategy_engine.signal_evaluator import strategy_signal_evaluator
from app.platform_core.strategy_engine.strategy_score import strategy_score_service
from app.v500_alpha41_strategy_scoring.models import StrategyScoringSummaryV500Alpha41

class StrategyScoringFacadeV500Alpha41:
    def summary(self): return StrategyScoringSummaryV500Alpha41()
    def signal_evaluation(self): return strategy_signal_evaluator.evaluate()
    def strategy_score(self): return strategy_score_service.score()
    def confidence(self): return strategy_confidence_model.confidence()
    def rules(self): return strategy_rule_evaluator.evaluate()
    def aggregate(self): return strategy_signal_aggregator.aggregate()
    def safety(self): return strategy_scoring_safety_policy.policy()
    def report(self): return strategy_scoring_report.report()
    def readiness(self): return strategy_scoring_readiness_gate.run()
    def contract(self): return {"ready": True, "strategy_engine": "package_b_signal_scoring", "execution_allowed": False}

strategy_scoring_facade_v500_alpha41 = StrategyScoringFacadeV500Alpha41()
