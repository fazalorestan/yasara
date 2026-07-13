class ExecutionCoreService:
    def status(self):
        return {
            "ready": True,
            "engine": "yasara_execution_engine",
            "mode": "dry_run_only",
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

execution_core_service = ExecutionCoreService()
