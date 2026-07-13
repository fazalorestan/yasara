from app.platform_core.backtest_engine.metrics import BacktestMetricsService

def test_v500_alpha29_metrics_win():
    r=BacktestMetricsService().calculate([{'pnl':10},{'pnl':-5}],10000); assert r['total_trades']==2 and r['win_rate']==50
