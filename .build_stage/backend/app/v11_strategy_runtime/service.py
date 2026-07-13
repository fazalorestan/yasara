from app.v11_strategy_runtime.context_builder import StrategyContextBuilderV11
from app.v11_strategy_runtime.models import StrategyContextV11, StrategyRuntimeSnapshotV11
from app.v11_strategy_runtime.rule_engine import StrategyRuleEngineV11
from app.v11_strategy_runtime.strategy_store import StrategyStoreV11


class StrategyRuntimeServiceV11:
    def __init__(self):
        self.store = StrategyStoreV11()
        self.engine = StrategyRuleEngineV11()
        self.context_builder = StrategyContextBuilderV11()
        self.signals = []

    def add_rule(self, rule):
        return self.store.add_rule(rule)

    def evaluate(self, context: StrategyContextV11):
        rules = self.store.seed_demo_rules()
        signal = self.engine.evaluate(rules, context)
        self.signals.append(signal)
        return signal

    def demo(self):
        context = self.context_builder.demo_context("BTCUSDT")
        return self.evaluate(context)

    def snapshot(self):
        self.store.seed_demo_rules()
        if not self.signals:
            self.demo()
        return StrategyRuntimeSnapshotV11(
            ready=True,
            rules=self.store.list_rules(),
            signals=self.signals,
        )
