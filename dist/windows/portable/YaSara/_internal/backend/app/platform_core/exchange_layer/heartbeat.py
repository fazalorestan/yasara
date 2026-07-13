class ExchangeHeartbeatMonitor:
    def heartbeat(self, exchange_id: str = "binance.sandbox"):
        return {
            "ready": True,
            "exchange_id": exchange_id,
            "alive": True,
            "last_seen_ms_ago": 0,
            "real_connection": False,
            "execution_allowed": False,
        }

    def timeout_check(self, last_seen_ms_ago: int, timeout_ms: int = 30000):
        return {"ready": True, "timed_out": last_seen_ms_ago > timeout_ms, "timeout_ms": timeout_ms}

exchange_heartbeat_monitor = ExchangeHeartbeatMonitor()
