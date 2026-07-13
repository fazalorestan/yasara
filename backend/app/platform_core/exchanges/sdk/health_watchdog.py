from app.platform_core.clock import utc_now_iso

class ExchangeConnectorHealthWatchdog:
    def __init__(self):
        self._metrics = {}

    def heartbeat(self, exchange_id: str, latency_ms: int = 0):
        item = self._metrics.setdefault(exchange_id, {
            "heartbeat_count": 0,
            "reconnect_count": 0,
            "failure_count": 0,
            "last_success": None,
            "last_error": None,
            "average_latency_ms": 0,
            "availability": 100.0,
        })
        item["heartbeat_count"] += 1
        item["last_success"] = utc_now_iso()
        item["average_latency_ms"] = latency_ms
        return {"ready": True, "exchange_id": exchange_id, "metrics": item}

    def record_failure(self, exchange_id: str, error: str):
        item = self._metrics.setdefault(exchange_id, {
            "heartbeat_count": 0,
            "reconnect_count": 0,
            "failure_count": 0,
            "last_success": None,
            "last_error": None,
            "average_latency_ms": 0,
            "availability": 100.0,
        })
        item["failure_count"] += 1
        item["last_error"] = error
        item["availability"] = max(0.0, 100.0 - item["failure_count"])
        return {"ready": True, "exchange_id": exchange_id, "metrics": item}

    def snapshot(self):
        return {"ready": True, "metrics": self._metrics}

exchange_connector_health_watchdog = ExchangeConnectorHealthWatchdog()
