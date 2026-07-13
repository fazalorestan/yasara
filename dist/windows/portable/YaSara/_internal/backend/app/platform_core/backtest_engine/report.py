from app.platform_core.backtest_engine.metrics import backtest_metrics_service

class BacktestReportBuilder:
    def build(self, trades: list[dict], initial_equity: float = 10000.0):
        metrics = backtest_metrics_service.calculate(trades, initial_equity)
        return {"ready": True, "metrics": metrics, "trades": trades, "real_execution": False, "auto_trading": False}

backtest_report_builder = BacktestReportBuilder()
