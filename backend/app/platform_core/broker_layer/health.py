class BrokerHealthService:
    def health(self, broker: dict):
        return {
            "ready": True,
            "broker_id": broker.get("broker_id"),
            "status": "ok" if broker.get("enabled", False) else "disabled",
            "latency_ms": 0,
            "connected": broker.get("enabled", False),
            "real_connection": False,
            "execution_allowed": False,
        }

broker_health_service = BrokerHealthService()
