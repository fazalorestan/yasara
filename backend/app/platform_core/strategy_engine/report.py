from app.platform_core.strategy_engine.rule_contract import strategy_rule_contract_service
from app.platform_core.strategy_engine.safety import strategy_safety_policy
from app.platform_core.strategy_engine.signal_contract import signal_contract_service
from app.platform_core.strategy_engine.strategy_contract import strategy_contract_service
from app.platform_core.strategy_engine.strategy_registry import strategy_registry

class StrategyCoreReport:
    def report(self):
        signal = signal_contract_service.signal()
        return {
            "ready": True,
            "strategies": strategy_registry.list_strategies(),
            "strategy_contract": strategy_contract_service.contract(),
            "dry_run": strategy_contract_service.dry_run(),
            "signal": signal,
            "signal_validation": signal_contract_service.validate(signal),
            "rules": strategy_rule_contract_service.rules(),
            "rule_validation": strategy_rule_contract_service.validate(),
            "safety": strategy_safety_policy.policy(),
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

strategy_core_report = StrategyCoreReport()
