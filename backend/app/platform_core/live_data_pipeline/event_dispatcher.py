class LiveStreamEventDispatcher:
    def dispatch_preview(self, event: dict | None = None):
        event = event or {"stream_id": "ticker.BTCUSDT", "symbol": "BTCUSDT", "price": 50000.0}
        return {"ready": True, "event": event, "dispatched": True, "mode": "simulated", "execution_allowed": False}
live_stream_event_dispatcher = LiveStreamEventDispatcher()
