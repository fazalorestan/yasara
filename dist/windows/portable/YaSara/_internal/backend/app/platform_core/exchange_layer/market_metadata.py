class ExchangeMarketMetadataService:
    def metadata(self, symbol: str = "BTCUSDT"):
        return {
            "ready": True,
            "symbol": symbol,
            "base_asset": symbol[:-4] if symbol.endswith("USDT") else symbol,
            "quote_asset": "USDT" if symbol.endswith("USDT") else "UNKNOWN",
            "price_precision": 2,
            "quantity_precision": 6,
            "min_notional": 5.0,
            "real_connection": False,
        }

exchange_market_metadata_service = ExchangeMarketMetadataService()
