from app.platform_core.backtest_engine.service import backtest_engine_foundation_service

class BacktestEngineReadinessGate:
    def run(self):
        cfg = backtest_engine_foundation_service.config()
        data = backtest_engine_foundation_service.dataset()
        report = backtest_engine_foundation_service.report()
        ready = cfg["ready"] and data["ready"] and report["ready"]
        return {"ready": ready, "checks": {"config_ready": cfg["ready"], "dataset_ready": data["ready"], "report_ready": report["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

backtest_engine_readiness_gate = BacktestEngineReadinessGate()
