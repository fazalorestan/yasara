class ExchangeRegistryService:
    def __init__(self):
        self._exchanges = {
            "binance.sandbox": {"exchange_id": "binance.sandbox", "name": "Binance Sandbox", "mode": "sandbox", "enabled": True},
            "bybit.sandbox": {"exchange_id": "bybit.sandbox", "name": "Bybit Sandbox", "mode": "sandbox", "enabled": True},
            "okx.sandbox": {"exchange_id": "okx.sandbox", "name": "OKX Sandbox", "mode": "sandbox", "enabled": True},
        }
    def list_exchanges(self): return {"ready": True, "exchanges": list(self._exchanges.values()), "count": len(self._exchanges)}
    def get(self, exchange_id: str): 
        exchange = self._exchanges.get(exchange_id)
        return {"ready": exchange is not None, "exchange": exchange}
    def register(self, exchange: dict):
        if not exchange.get("exchange_id"): return {"ready": False, "registered": False, "reason": "missing_exchange_id"}
        self._exchanges[exchange["exchange_id"]] = exchange
        return {"ready": True, "registered": True, "exchange_id": exchange["exchange_id"]}
exchange_registry_service = ExchangeRegistryService()
