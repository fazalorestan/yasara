class ExchangeCapabilityService:
    def detect(self, exchange: dict):
        exchange_id = exchange.get("exchange_id", "")
        return {"ready": True, "exchange_id": exchange_id, "spot": True, "futures": "binance" in exchange_id or "bybit" in exchange_id, "margin": False, "websocket": True, "real_connection": False, "execution_allowed": False}
    def matrix(self, exchanges: list[dict]):
        return {"ready": True, "items": [self.detect(e) for e in exchanges]}
exchange_capability_service = ExchangeCapabilityService()
