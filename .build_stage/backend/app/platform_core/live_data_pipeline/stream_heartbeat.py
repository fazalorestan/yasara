class LiveStreamHeartbeat:
    def ping(self, stream_id: str = "ticker.BTCUSDT"):
        return {"ready": True, "stream_id": stream_id, "alive": True, "last_message_ms_ago": 0, "real_connection": False}
    def timeout_check(self, last_message_ms_ago: int, timeout_ms: int = 30000):
        return {"ready": True, "timed_out": last_message_ms_ago > timeout_ms, "timeout_ms": timeout_ms}
live_stream_heartbeat = LiveStreamHeartbeat()
