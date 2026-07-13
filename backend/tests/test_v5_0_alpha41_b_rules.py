from app.platform_core.strategy_engine.rule_evaluator import StrategyRuleEvaluator

def test_v500_alpha41_b_rules(): assert StrategyRuleEvaluator().evaluate()['rules_passed'] is True
