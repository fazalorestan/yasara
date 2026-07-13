class ExchangeSymbolRegistryService:
    def symbols(self, exchange_id: str = "binance.sandbox"):
        return {
            "ready": True,
            "exchange_id": exchange_id,
            "symbols": ["BTCUSDT", "ETHUSDT", "BNBUSDT"],
            "real_connection": False,
        }

    def normalize(self, symbol: str):
        return {"ready": True, "symbol": str(symbol).replace("/", "").upper()}

exchange_symbol_registry_service = ExchangeSymbolRegistryService()
