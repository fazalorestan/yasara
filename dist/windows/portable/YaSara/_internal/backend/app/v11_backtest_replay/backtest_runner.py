from app.v11_backtest_replay.models import BacktestRunResultV11, BacktestTradeV11, ReplayDatasetV11
from app.v11_backtest_replay.performance import BacktestPerformanceAnalyzerV11
from app.v11_backtest_replay.replay_engine import PaperReplayEngineV11
from app.v11_strategy_runtime.models import StrategyContextV11, StrategyActionV11
from app.v11_strategy_runtime.service import StrategyRuntimeServiceV11


class BacktestRunnerV11:
    def __init__(self):
        self.replay = PaperReplayEngineV11()
        self.strategy = StrategyRuntimeServiceV11()
        self.performance = BacktestPerformanceAnalyzerV11()

    def run(self, dataset: ReplayDatasetV11, quantity: float = 1.0) -> BacktestRunResultV11:
        trades: list[BacktestTradeV11] = []
        in_position = False

        for candle in self.replay.replay(dataset):
            context = StrategyContextV11(
                symbol=candle.symbol,
                price=candle.close,
                ai_score=0.8 if candle.close >= candle.open else 0.2,
                risk_allowed=True,
            )
            signal = self.strategy.evaluate(context)
            if signal.action == StrategyActionV11.BUY and not in_position:
                trades.append(BacktestTradeV11(
                    symbol=candle.symbol,
                    action="buy",
                    price=candle.close,
                    quantity=quantity,
                    timestamp=candle.timestamp,
                    reason=signal.reason,
                ))
                in_position = True
            elif signal.action == StrategyActionV11.SELL and in_position:
                trades.append(BacktestTradeV11(
                    symbol=candle.symbol,
                    action="sell",
                    price=candle.close,
                    quantity=quantity,
                    timestamp=candle.timestamp,
                    reason=signal.reason,
                ))
                in_position = False

        if in_position and dataset.candles:
            last = dataset.candles[-1]
            trades.append(BacktestTradeV11(
                symbol=last.symbol,
                action="sell",
                price=last.close,
                quantity=quantity,
                timestamp=last.timestamp,
                reason="close_open_position_at_end",
            ))

        metrics = self.performance.calculate(trades)
        return BacktestRunResultV11(
            ready=True,
            symbol=dataset.symbol,
            trades=trades,
            metrics=metrics,
        )
