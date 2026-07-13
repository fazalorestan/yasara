class ExchangeOrderbookSnapshotService:
    def orderbook(self, symbol: str = "BTCUSDT", depth: int = 5):
        bids = [[50000.0 - i, 1.0 + i * 0.1] for i in range(depth)]
        asks = [[50001.0 + i, 1.0 + i * 0.1] for i in range(depth)]
        return {
            "ready": True,
            "symbol": symbol,
            "depth": depth,
            "bids": bids,
            "asks": asks,
            "source": "simulated",
            "real_connection": False,
        }

exchange_orderbook_snapshot_service = ExchangeOrderbookSnapshotService()
