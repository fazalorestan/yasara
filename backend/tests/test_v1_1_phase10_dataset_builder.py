from app.v11_backtest_replay.dataset_builder import ReplayDatasetBuilderV11

def test_replay_dataset_builder():
    dataset = ReplayDatasetBuilderV11().build_demo_dataset("BTCUSDT")
    assert dataset.symbol == "BTCUSDT"
    assert len(dataset.candles) >= 5
