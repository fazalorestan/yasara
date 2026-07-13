class ExchangeMarketTypeService:
    def supported_market_types(self, exchange_id: str = "binance.sandbox"):
        types = ["spot"]
        if "binance" in exchange_id or "bybit" in exchange_id:
            types.append("futures")
        return {"ready": True, "exchange_id": exchange_id, "market_types": types, "real_connection": False}
exchange_market_type_service = ExchangeMarketTypeService()
