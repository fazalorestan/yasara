from app.platform_core.market_data.models import MarketSnapshot, OHLCV, OrderBookLevel, OrderBookSnapshot, TradeTick

class MarketDataSnapshotService:
    def sample_ohlcv(self, symbol: str = "BTCUSDT"):
        return OHLCV(symbol=symbol, timeframe="1h", open_time=1, open=100.0, high=110.0, low=95.0, close=105.0, volume=1000.0).__dict__

    def sample_orderbook(self, symbol: str = "BTCUSDT"):
        book = OrderBookSnapshot(
            symbol=symbol,
            bids=[OrderBookLevel(price=104.0, quantity=2.0), OrderBookLevel(price=103.5, quantity=3.0)],
            asks=[OrderBookLevel(price=105.0, quantity=2.5), OrderBookLevel(price=105.5, quantity=1.0)],
        )
        return book.__dict__ | {"bids": [x.__dict__ for x in book.bids], "asks": [x.__dict__ for x in book.asks]}

    def sample_trade(self, symbol: str = "BTCUSDT"):
        return TradeTick(symbol=symbol, price=105.0, quantity=0.5, side="buy").__dict__

    def sample_snapshot(self, symbol: str = "BTCUSDT"):
        return MarketSnapshot(symbol=symbol, last_price=105.0, change_24h=2.5, volume_24h=10000.0).__dict__

market_data_snapshot_service = MarketDataSnapshotService()
