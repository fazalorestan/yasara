from time import time
from app.v11_backtest_replay.models import ReplayCandleV11, ReplayDatasetV11


class ReplayDatasetBuilderV11:
    def build_demo_dataset(self, symbol: str = "BTCUSDT") -> ReplayDatasetV11:
        now = time()
        prices = [100, 102, 105, 103, 108, 112, 109, 115, 118, 116]
        candles = []
        for idx, close in enumerate(prices):
            open_price = prices[idx - 1] if idx else close
            candles.append(ReplayCandleV11(
                symbol=symbol.upper(),
                timestamp=now + idx * 60,
                open=open_price,
                high=max(open_price, close) + 1,
                low=min(open_price, close) - 1,
                close=close,
                volume=100 + idx,
            ))
        return ReplayDatasetV11(symbol=symbol.upper(), candles=candles)
