from app.platform_core.broker_layer.service import broker_layer_core_service

class BrokerLayerCoreReadinessGate:
    def run(self):
        contract = broker_layer_core_service.contract()
        brokers = broker_layer_core_service.brokers()
        capabilities = broker_layer_core_service.capabilities()
        health = broker_layer_core_service.health()
        safety = broker_layer_core_service.safety()
        ready = contract["ready"] and brokers["ready"] and capabilities["ready"] and health["ready"] and safety["ready"]
        return {
            "ready": ready,
            "checks": {
                "contract_ready": contract["ready"],
                "brokers_ready": brokers["ready"],
                "capabilities_ready": capabilities["ready"],
                "health_ready": health["ready"],
                "safety_ready": safety["ready"],
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

broker_layer_core_readiness_gate = BrokerLayerCoreReadinessGate()
