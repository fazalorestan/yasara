class DryRunExecutorService:
    def execute(self, intent: dict | None = None):
        intent = intent or {"symbol": "BTCUSDT", "side": "hold", "quantity": 0.0}
        return {
            "ready": True,
            "intent": intent,
            "dry_run": True,
            "executed": False,
            "order_id": None,
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

dry_run_executor_service = DryRunExecutorService()
