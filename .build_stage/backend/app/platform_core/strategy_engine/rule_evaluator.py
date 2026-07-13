class StrategyRuleEvaluator:
    def evaluate(self):
        return {
            "ready": True,
            "rules_passed": True,
            "rules": [
                {"rule_id": "execution.disabled", "passed": True},
                {"rule_id": "risk.required", "passed": True},
            ],
            "execution_allowed": False,
        }

strategy_rule_evaluator = StrategyRuleEvaluator()
