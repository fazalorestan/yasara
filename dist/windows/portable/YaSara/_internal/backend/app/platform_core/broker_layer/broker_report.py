from app.platform_core.broker_layer.broker_adapter_contract import broker_adapter_contract_service
from app.platform_core.broker_layer.broker_capability import broker_capability_service
from app.platform_core.broker_layer.broker_registry import broker_registry
from app.platform_core.broker_layer.broker_safety import broker_safety_policy

class BrokerCoreReport:
    def report(self):
        return {
            "ready": True,
            "brokers": broker_registry.list_brokers(),
            "adapter_contract": broker_adapter_contract_service.contract(),
            "dry_connect": broker_adapter_contract_service.dry_connect(),
            "capabilities": broker_capability_service.capabilities(),
            "safety": broker_safety_policy.policy(),
            "real_broker_connection_enabled": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

broker_core_report = BrokerCoreReport()
