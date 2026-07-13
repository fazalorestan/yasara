class ExchangeTickerSnapshotService:
    def ticker(self, symbol: str = "BTCUSDT"):
        return {
            "ready": True,
            "symbol": symbol,
            "last_price": 50000.0,
            "bid": 49999.0,
            "ask": 50001.0,
            "volume_24h": 1000.0,
            "source": "simulated",
            "real_connection": False,
        }

exchange_ticker_snapshot_service = ExchangeTickerSnapshotService()
