from app.v11_backtest_replay.models import ReplayCandleV11, ReplayDatasetV11


class PaperReplayEngineV11:
    def replay(self, dataset: ReplayDatasetV11):
        for candle in dataset.candles:
            yield candle

    def latest_price(self, candle: ReplayCandleV11) -> float:
        return candle.close
