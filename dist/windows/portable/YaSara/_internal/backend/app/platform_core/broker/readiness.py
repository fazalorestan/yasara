from app.platform_core.broker.service import broker_layer_foundation_service

class BrokerLayerReadinessGate:
    def run(self):
        cap = broker_layer_foundation_service.capabilities()
        safe = broker_layer_foundation_service.safety_policy()
        pre = broker_layer_foundation_service.preflight_order({"symbol":"BTCUSDT","side":"buy","order_type":"market","quantity":0.1})
        ready = cap["ready"] and safe["ready"] and pre["ready"]
        return {"ready": ready, "checks": {"capabilities_ready": cap["ready"], "safety_ready": safe["ready"], "execution_guard_ready": pre["ready"], "live_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
broker_layer_readiness_gate = BrokerLayerReadinessGate()
