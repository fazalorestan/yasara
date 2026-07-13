from app.platform_core.backtest_engine.report import BacktestReportBuilder

def test_v500_alpha29_report(): assert BacktestReportBuilder().build([{'pnl':1}])['ready'] is True
