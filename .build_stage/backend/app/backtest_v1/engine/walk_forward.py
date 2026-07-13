from datetime import timedelta
from app.backtest_v1.domain.models import BacktestConfig, WalkForwardWindow
from app.backtest_v1.engine.backtest_engine import BacktestEngineV1
from app.market_data.domain.models import Candle

class WalkForwardEngineV1:
    def build_windows(self, candles: list[Candle], train_size: int = 300, test_size: int = 100) -> list[WalkForwardWindow]:
        windows = []
        i = 0
        while i + train_size + test_size <= len(candles):
            train = candles[i:i+train_size]
            test = candles[i+train_size:i+train_size+test_size]
            windows.append(WalkForwardWindow(
                train_start=train[0].open_time,
                train_end=train[-1].close_time,
                test_start=test[0].open_time,
                test_end=test[-1].close_time,
            ))
            i += test_size
        return windows

    def run(self, config: BacktestConfig, candles: list[Candle], train_size: int = 300, test_size: int = 100) -> list[WalkForwardWindow]:
        windows = self.build_windows(candles, train_size, test_size)
        engine = BacktestEngineV1()
        for idx, window in enumerate(windows):
            start = idx * test_size + train_size
            test = candles[start:start+test_size]
            window.report = engine.run(config, test)
        return windows
