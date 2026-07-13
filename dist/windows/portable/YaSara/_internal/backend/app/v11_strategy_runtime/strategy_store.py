from app.v11_strategy_runtime.models import StrategyConditionTypeV11, StrategyConditionV11, StrategyRuleV11, StrategyActionV11


class StrategyStoreV11:
    def __init__(self):
        self.rules: list[StrategyRuleV11] = []

    def add_rule(self, rule: StrategyRuleV11) -> StrategyRuleV11:
        self.rules.append(rule)
        return rule

    def list_rules(self) -> list[StrategyRuleV11]:
        return self.rules

    def seed_demo_rules(self) -> list[StrategyRuleV11]:
        if self.rules:
            return self.rules
        self.add_rule(StrategyRuleV11(
            name="BTC bullish AI guarded buy",
            action=StrategyActionV11.BUY,
            conditions=[
                StrategyConditionV11(condition_type=StrategyConditionTypeV11.PRICE_ABOVE, symbol="BTCUSDT", value=100),
                StrategyConditionV11(condition_type=StrategyConditionTypeV11.AI_SCORE_ABOVE, symbol="BTCUSDT", value=0.6),
                StrategyConditionV11(condition_type=StrategyConditionTypeV11.RISK_ALLOWED, value=True),
            ],
        ))
        self.add_rule(StrategyRuleV11(
            name="BTC defensive sell",
            action=StrategyActionV11.SELL,
            conditions=[
                StrategyConditionV11(condition_type=StrategyConditionTypeV11.PRICE_BELOW, symbol="BTCUSDT", value=90),
                StrategyConditionV11(condition_type=StrategyConditionTypeV11.RISK_ALLOWED, value=True),
            ],
        ))
        return self.rules
