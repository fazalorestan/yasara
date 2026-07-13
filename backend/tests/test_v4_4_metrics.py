from app.v44_backtest_benchmark import metrics

def test_v44_metrics():
    trades = [{"pnl": 10, "pnl_percent": 1}, {"pnl": -5, "pnl_percent": -0.5}, {"pnl": 20, "pnl_percent": 2}]
    curve = [100, 110, 105, 125]
    assert metrics.win_rate(trades) > 0
    assert metrics.profit_factor(trades) > 0
    assert metrics.max_drawdown(curve) >= 0
    assert "net_profit" in metrics.stats(trades, curve, 100, 125)
