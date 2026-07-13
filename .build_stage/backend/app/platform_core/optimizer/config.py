class OptimizerConfigService:
    def default(self):
        return {"ready": True, "strategy_id": "demo_strategy", "symbol": "BTCUSDT", "objective": "net_pnl", "max_trials": 20, "execution_allowed": False}

optimizer_config_service = OptimizerConfigService()
