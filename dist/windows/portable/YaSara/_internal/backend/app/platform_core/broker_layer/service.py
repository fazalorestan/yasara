from app.platform_core.broker_layer.capabilities import broker_capability_service
from app.platform_core.broker_layer.contract import broker_contract_service
from app.platform_core.broker_layer.health import broker_health_service
from app.platform_core.broker_layer.registry import broker_registry_service
from app.platform_core.broker_layer.safety import broker_execution_safety_contract

class BrokerLayerCoreService:
    def contract(self): return broker_contract_service.contract()
    def brokers(self): return broker_registry_service.list_brokers()
    def default_broker(self): return broker_registry_service.get("paper.demo")
    def capabilities(self):
        return broker_capability_service.matrix(self.brokers()["brokers"])
    def health(self):
        return {"ready": True, "items": [broker_health_service.health(b) for b in self.brokers()["brokers"]]}
    def safety(self): return broker_execution_safety_contract.policy()
    def status(self):
        return {
            "ready": True,
            "brokers_ready": self.brokers()["ready"],
            "capabilities_ready": self.capabilities()["ready"],
            "health_ready": self.health()["ready"],
            "execution_allowed": False,
        }

broker_layer_core_service = BrokerLayerCoreService()
