from app.v11_backtest_replay.dataset_builder import ReplayDatasetBuilderV11
from app.v11_backtest_replay.replay_engine import PaperReplayEngineV11

def test_paper_replay_engine():
    dataset = ReplayDatasetBuilderV11().build_demo_dataset()
    candles = list(PaperReplayEngineV11().replay(dataset))
    assert len(candles) == len(dataset.candles)
