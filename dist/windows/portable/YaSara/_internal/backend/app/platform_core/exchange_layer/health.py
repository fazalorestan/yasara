class ExchangeHealthService:
    def health(self, exchange: dict):
        return {"ready": True, "exchange_id": exchange.get("exchange_id"), "status": "ok" if exchange.get("enabled", False) else "disabled", "latency_ms": 0, "connected": exchange.get("enabled", False), "real_connection": False, "execution_allowed": False}
exchange_health_service = ExchangeHealthService()
