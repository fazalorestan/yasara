class BrokerRegistryService:
    def __init__(self):
        self._brokers = {
            "paper.demo": {"broker_id": "paper.demo", "name": "Paper Demo Broker", "mode": "paper", "enabled": True},
            "sandbox.demo": {"broker_id": "sandbox.demo", "name": "Sandbox Demo Broker", "mode": "sandbox", "enabled": True},
        }

    def list_brokers(self):
        return {"ready": True, "brokers": list(self._brokers.values()), "count": len(self._brokers)}

    def get(self, broker_id: str):
        broker = self._brokers.get(broker_id)
        return {"ready": broker is not None, "broker": broker}

    def register(self, broker: dict):
        if not broker.get("broker_id"):
            return {"ready": False, "registered": False, "reason": "missing_broker_id"}
        self._brokers[broker["broker_id"]] = broker
        return {"ready": True, "registered": True, "broker_id": broker["broker_id"]}

broker_registry_service = BrokerRegistryService()
