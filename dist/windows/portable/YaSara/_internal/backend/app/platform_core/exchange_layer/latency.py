class ExchangeLatencyMonitor:
    def ping(self, exchange_id: str = "binance.sandbox"):
        return {
            "ready": True,
            "exchange_id": exchange_id,
            "latency_ms": 0,
            "source": "simulated",
            "real_connection": False,
        }

    def latency_grade(self, latency_ms: float):
        grade = "excellent" if latency_ms <= 50 else "good" if latency_ms <= 150 else "degraded"
        return {"ready": True, "latency_ms": latency_ms, "grade": grade}

exchange_latency_monitor = ExchangeLatencyMonitor()
