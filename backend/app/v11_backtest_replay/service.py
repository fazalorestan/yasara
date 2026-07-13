from app.v11_backtest_replay.backtest_runner import BacktestRunnerV11
from app.v11_backtest_replay.dataset_builder import ReplayDatasetBuilderV11


class BacktestReplayServiceV11:
    def __init__(self):
        self.datasets = ReplayDatasetBuilderV11()
        self.runner = BacktestRunnerV11()

    def demo_dataset(self, symbol: str = "BTCUSDT"):
        return self.datasets.build_demo_dataset(symbol)

    def run_demo(self, symbol: str = "BTCUSDT"):
        dataset = self.demo_dataset(symbol)
        return self.runner.run(dataset)

    def summary_payload(self) -> dict:
        result = self.run_demo()
        return {
            "ready": result.ready,
            "symbol": result.symbol,
            "total_trades": result.metrics.total_trades,
            "final_equity": result.metrics.final_equity,
            "safety": result.safety,
        }
