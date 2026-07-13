class BrokerLatencyMonitor:
    def ping(self, broker_id: str = "paper.demo"):
        return {"ready": True, "broker_id": broker_id, "latency_ms": 0, "source": "simulated", "real_connection": False}
    def latency_grade(self, latency_ms: float):
        grade = "excellent" if latency_ms <= 50 else "good" if latency_ms <= 150 else "degraded"
        return {"ready": True, "latency_ms": latency_ms, "grade": grade}
broker_latency_monitor = BrokerLatencyMonitor()
