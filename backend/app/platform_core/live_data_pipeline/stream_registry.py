class LiveStreamRegistry:
    def __init__(self):
        self._streams = {
            "ticker.BTCUSDT": {"stream_id": "ticker.BTCUSDT", "type": "ticker", "symbol": "BTCUSDT", "enabled": True},
            "orderbook.BTCUSDT": {"stream_id": "orderbook.BTCUSDT", "type": "orderbook", "symbol": "BTCUSDT", "enabled": True},
            "candles.BTCUSDT.1h": {"stream_id": "candles.BTCUSDT.1h", "type": "candles", "symbol": "BTCUSDT", "timeframe": "1h", "enabled": True},
        }
    def list_streams(self): return {"ready": True, "streams": list(self._streams.values()), "count": len(self._streams)}
    def get(self, stream_id: str):
        stream = self._streams.get(stream_id)
        return {"ready": stream is not None, "stream": stream}
live_stream_registry = LiveStreamRegistry()
