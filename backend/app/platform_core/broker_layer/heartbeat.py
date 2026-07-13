class BrokerHeartbeatMonitor:
    def heartbeat(self, broker_id: str = "paper.demo"):
        return {"ready": True, "broker_id": broker_id, "alive": True, "last_seen_ms_ago": 0, "real_connection": False, "execution_allowed": False}
    def timeout_check(self, last_seen_ms_ago: int, timeout_ms: int = 30000):
        return {"ready": True, "timed_out": last_seen_ms_ago > timeout_ms, "timeout_ms": timeout_ms}
broker_heartbeat_monitor = BrokerHeartbeatMonitor()
