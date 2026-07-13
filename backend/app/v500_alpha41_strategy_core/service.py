from app.platform_core.strategy_engine.readiness import strategy_core_readiness_gate
from app.platform_core.strategy_engine.report import strategy_core_report
from app.platform_core.strategy_engine.rule_contract import strategy_rule_contract_service
from app.platform_core.strategy_engine.safety import strategy_safety_policy
from app.platform_core.strategy_engine.signal_contract import signal_contract_service
from app.platform_core.strategy_engine.strategy_contract import strategy_contract_service
from app.platform_core.strategy_engine.strategy_registry import strategy_registry
from app.v500_alpha41_strategy_core.models import StrategyCoreSummaryV500Alpha41

class StrategyCoreFacadeV500Alpha41:
    def summary(self): return StrategyCoreSummaryV500Alpha41()
    def strategies(self): return strategy_registry.list_strategies()
    def strategy_contract(self): return strategy_contract_service.contract()
    def dry_run(self): return strategy_contract_service.dry_run()
    def signal(self): return signal_contract_service.signal()
    def rules(self): return strategy_rule_contract_service.rules()
    def safety(self): return strategy_safety_policy.policy()
    def report(self): return strategy_core_report.report()
    def readiness(self): return strategy_core_readiness_gate.run()
    def contract(self): return {"ready": True, "strategy_engine": "package_a_core_contract", "execution_allowed": False}

strategy_core_facade_v500_alpha41 = StrategyCoreFacadeV500Alpha41()
