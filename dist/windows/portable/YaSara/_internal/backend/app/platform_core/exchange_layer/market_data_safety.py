class ExchangeMarketDataSafetyService:
    def policy(self):
        return {
            "ready": True,
            "market_data_only": True,
            "real_exchange_connection": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

    def validate_symbol(self, symbol: str):
        normalized = str(symbol).replace("/", "").upper()
        valid = normalized.endswith("USDT") and len(normalized) >= 7
        return {"ready": True, "symbol": normalized, "valid": valid}

exchange_market_data_safety_service = ExchangeMarketDataSafetyService()
