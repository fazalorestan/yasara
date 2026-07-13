from app.platform_core.backtest_engine.service import backtest_engine_foundation_service

class OptimizerBacktestLinkService:
    def link(self):
        report = backtest_engine_foundation_service.report()
        return {"ready": True, "backtest_ready": report["ready"], "execution_allowed": False}

optimizer_backtest_link_service = OptimizerBacktestLinkService()
