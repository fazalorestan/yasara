class BrokerCapabilityService:
    def detect(self, broker: dict):
        mode = broker.get("mode", "paper")
        paper_like = mode in ["paper", "sandbox"]
        return {
            "ready": True,
            "broker_id": broker.get("broker_id"),
            "supports_market_orders": paper_like,
            "supports_limit_orders": paper_like,
            "supports_positions": paper_like,
            "supports_balances": True,
            "real_execution_capable": False,
            "execution_allowed": False,
        }

    def matrix(self, brokers: list[dict]):
        return {"ready": True, "items": [self.detect(b) for b in brokers]}

broker_capability_service = BrokerCapabilityService()
