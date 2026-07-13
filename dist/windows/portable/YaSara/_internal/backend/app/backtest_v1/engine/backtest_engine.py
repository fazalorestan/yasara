from app.backtest_v1.domain.models import BacktestConfig, BacktestReport
from app.backtest_v1.engine.metrics import BacktestMetricsEngineV1
from app.backtest_v1.engine.replay import CandleReplayEngineV1
from app.market_data.domain.models import Candle

class BacktestEngineV1:
    def __init__(self):
        self.replay = CandleReplayEngineV1()
        self.metrics = BacktestMetricsEngineV1()

    def run(self, config: BacktestConfig, candles: list[Candle]) -> BacktestReport:
        warnings = []
        if len(candles) < 50:
            warnings.append("Low candle count; results are not reliable.")
        trades, equity_curve = self.replay.run_simple_breakout(config, candles)
        metrics = self.metrics.calculate(config.initial_capital, trades, equity_curve)
        return BacktestReport(config=config, metrics=metrics, trades=trades, equity_curve=equity_curve, warnings=warnings)
