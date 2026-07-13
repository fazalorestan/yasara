from app.platform_core.execution_engine.cancellation_contract import cancellation_contract_service
from app.platform_core.execution_engine.execution_journal import execution_journal_service
from app.platform_core.execution_engine.execution_state_machine import execution_state_machine
from app.platform_core.execution_engine.fill_contract import fill_contract_service
from app.platform_core.execution_engine.lifecycle_safety import execution_lifecycle_safety_policy
from app.platform_core.execution_engine.order_lifecycle import order_lifecycle_service

class ExecutionLifecycleReport:
    def report(self):
        return {
            "ready": True,
            "initial_state": execution_state_machine.initial(),
            "transition": execution_state_machine.transition(),
            "lifecycle": order_lifecycle_service.lifecycle(),
            "journal": execution_journal_service.append(),
            "fill_contract": fill_contract_service.contract(),
            "simulated_fill": fill_contract_service.simulated_fill(),
            "cancellation_contract": cancellation_contract_service.contract(),
            "dry_cancel": cancellation_contract_service.dry_cancel(),
            "safety": execution_lifecycle_safety_policy.policy(),
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

execution_lifecycle_report = ExecutionLifecycleReport()
