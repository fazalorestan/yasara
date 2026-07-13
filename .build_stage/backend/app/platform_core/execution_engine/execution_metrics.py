class ExecutionMetricsService:
    def metrics(self):
        return {
            "ready": True,
            "orders_total": 0,
            "orders_dry_run": 0,
            "orders_real": 0,
            "failed_orders": 0,
            "avg_latency_ms": 0.0,
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

execution_metrics_service = ExecutionMetricsService()
