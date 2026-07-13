from app.v11_backtest_replay.dataset_builder import ReplayDatasetBuilderV11
from app.v11_backtest_replay.backtest_runner import BacktestRunnerV11

def test_backtest_runner():
    result = BacktestRunnerV11().run(ReplayDatasetBuilderV11().build_demo_dataset())
    assert result.ready is True
    assert result.metrics.total_trades >= 1
