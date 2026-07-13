class BrokerLatencyMonitorService:
    def latency(self):
        return {
            "ready": True,
            "latency_ms": 0.0,
            "source": "simulated",
            "within_threshold": True,
            "real_network_call": False,
            "execution_allowed": False,
        }

broker_latency_monitor_service = BrokerLatencyMonitorService()
