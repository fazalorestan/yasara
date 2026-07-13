class StrategyRuleEngineV33:
    def resolve_value(self, key, fields):
        if isinstance(key, (int, float, bool)):
            return key
        if isinstance(key, str):
            if key in fields:
                return fields[key]
            try:
                return float(key)
            except ValueError:
                return key
        return key

    def compare(self, left, operator, right):
        if operator == "gt":
            return left > right
        if operator == "gte":
            return left >= right
        if operator == "lt":
            return left < right
        if operator == "lte":
            return left <= right
        if operator == "eq":
            return left == right
        if operator == "neq":
            return left != right
        return False

    def evaluate_rule(self, rule, fields):
        if not rule.enabled:
            return {"rule_id": rule.rule_id, "matched": False, "action": "hold", "reason": "disabled"}

        results = []
        for condition in rule.conditions:
            left = self.resolve_value(condition.left, fields)
            right = self.resolve_value(condition.right, fields)
            matched = self.compare(left, condition.operator, right)
            results.append({
                "left": condition.left,
                "operator": condition.operator,
                "right": condition.right,
                "left_value": left,
                "right_value": right,
                "matched": matched,
            })

        matched_all = all(item["matched"] for item in results) if results else False
        return {
            "rule_id": rule.rule_id,
            "name": rule.name,
            "matched": matched_all,
            "action": rule.action if matched_all else "hold",
            "conditions": results,
        }

    def evaluate_strategy(self, strategy, fields):
        evaluations = [self.evaluate_rule(rule, fields) for rule in strategy.rules]
        action = "hold"
        matched_rules = [item for item in evaluations if item["matched"]]
        if matched_rules:
            action = matched_rules[0]["action"]

        return {
            "ready": True,
            "strategy_id": strategy.strategy_id,
            "strategy_name": strategy.name,
            "action": action,
            "matched_rules": matched_rules,
            "evaluations": evaluations,
            "live_trading_enabled": False,
        }
