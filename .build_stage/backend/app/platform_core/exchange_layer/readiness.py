from app.platform_core.exchange_layer.service import exchange_layer_core_service
class ExchangeLayerCoreReadinessGate:
    def run(self):
        contract = exchange_layer_core_service.contract()
        exchanges = exchange_layer_core_service.exchanges()
        capabilities = exchange_layer_core_service.capabilities()
        health = exchange_layer_core_service.health()
        safety = exchange_layer_core_service.safety()
        ready = contract["ready"] and exchanges["ready"] and capabilities["ready"] and health["ready"] and safety["ready"]
        return {"ready": ready, "checks": {"contract_ready": contract["ready"], "exchanges_ready": exchanges["ready"], "capabilities_ready": capabilities["ready"], "health_ready": health["ready"], "safety_ready": safety["ready"], "real_exchange_connection_allowed": False, "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
exchange_layer_core_readiness_gate = ExchangeLayerCoreReadinessGate()
