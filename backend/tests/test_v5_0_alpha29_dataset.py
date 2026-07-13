from app.platform_core.backtest_engine.dataset import HistoricalDatasetContract

def test_v500_alpha29_dataset(): assert len(HistoricalDatasetContract().sample()['candles']) == 3
