class BrokerRegistry:
    def __init__(self):
        self._brokers = {
            "sim.broker": {"broker_id": "sim.broker", "name": "Simulated Broker", "mode": "simulated", "enabled": True},
            "paper.broker": {"broker_id": "paper.broker", "name": "Paper Broker Contract", "mode": "paper_contract", "enabled": True},
        }

    def list_brokers(self):
        return {"ready": True, "brokers": list(self._brokers.values()), "count": len(self._brokers)}

    def get(self, broker_id: str):
        broker = self._brokers.get(broker_id)
        return {"ready": broker is not None, "broker": broker}

broker_registry = BrokerRegistry()
