from app.v11_backtest_replay.models import BacktestTradeV11
from app.v11_backtest_replay.performance import BacktestPerformanceAnalyzerV11

def test_backtest_performance_metrics():
    trades = [
        BacktestTradeV11(symbol="BTCUSDT", action="buy", price=100, quantity=1, timestamp=1),
        BacktestTradeV11(symbol="BTCUSDT", action="sell", price=110, quantity=1, timestamp=2),
    ]
    metrics = BacktestPerformanceAnalyzerV11().calculate(trades)
    assert metrics.realized_pnl == 10
    assert metrics.winning_trades == 1
