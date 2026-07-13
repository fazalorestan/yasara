class LiveStreamMetricsService:
    def metrics(self):
        return {"ready": True, "throughput_per_sec": 0, "queue_size": 0, "dropped_messages": 0, "latency_ms": 0, "processing_time_ms": 0, "source": "simulated"}
live_stream_metrics_service = LiveStreamMetricsService()
