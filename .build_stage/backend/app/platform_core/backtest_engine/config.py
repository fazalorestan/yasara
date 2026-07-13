class BacktestConfigService:
    def default(self):
        return {"ready": True, "strategy_id": "demo_strategy", "symbol": "BTCUSDT", "timeframe": "1h", "initial_equity": 10000.0, "fee_pct": 0.1, "slippage_pct": 0.05, "risk_pct": 1.0}

backtest_config_service = BacktestConfigService()
