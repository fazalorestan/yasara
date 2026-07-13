from app.platform_core.backtest_engine.metrics import BacktestMetricsService

def test_v500_alpha29_metrics_empty(): assert BacktestMetricsService().calculate([])['win_rate'] == 0.0
