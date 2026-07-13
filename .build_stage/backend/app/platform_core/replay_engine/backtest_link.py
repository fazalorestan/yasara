from app.platform_core.backtest_engine.service import backtest_engine_foundation_service

class ReplayBacktestLinkService:
    def link(self):
        report = backtest_engine_foundation_service.report()
        return {"ready": True, "backtest_report_ready": report["ready"], "linked_trades": len(report["trades"]), "execution_allowed": False}

replay_backtest_link_service = ReplayBacktestLinkService()
