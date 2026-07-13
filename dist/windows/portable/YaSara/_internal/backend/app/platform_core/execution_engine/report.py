from app.platform_core.execution_engine.dry_run_executor import dry_run_executor_service
from app.platform_core.execution_engine.execution_core import execution_core_service
from app.platform_core.execution_engine.execution_safety import execution_safety_policy
from app.platform_core.execution_engine.order_contract import order_contract_service
from app.platform_core.execution_engine.order_intent import order_intent_service

class ExecutionCoreReport:
    def report(self):
        intent = order_intent_service.intent()
        return {
            "ready": True,
            "core": execution_core_service.status(),
            "order_contract": order_contract_service.contract(),
            "intent": intent,
            "intent_validation": order_intent_service.validate(intent),
            "dry_run": dry_run_executor_service.execute(intent),
            "safety": execution_safety_policy.policy(),
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

execution_core_report = ExecutionCoreReport()
