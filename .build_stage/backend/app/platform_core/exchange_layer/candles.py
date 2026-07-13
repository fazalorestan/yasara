class ExchangeCandleContractService:
    def candles(self, symbol: str = "BTCUSDT", timeframe: str = "1h", limit: int = 5):
        rows = []
        for i in range(limit):
            open_price = 50000.0 + i * 10.0
            rows.append({
                "timestamp": i,
                "open": open_price,
                "high": open_price + 100.0,
                "low": open_price - 100.0,
                "close": open_price + 50.0,
                "volume": 10.0 + i,
            })
        return {
            "ready": True,
            "symbol": symbol,
            "timeframe": timeframe,
            "limit": limit,
            "candles": rows,
            "source": "simulated",
            "real_connection": False,
        }

exchange_candle_contract_service = ExchangeCandleContractService()
