from app.v11_strategy_runtime.service import StrategyRuntimeServiceV11

def test_strategy_runtime_snapshot():
    snapshot = StrategyRuntimeServiceV11().snapshot()
    assert snapshot.ready is True
    assert len(snapshot.rules) >= 1
    assert len(snapshot.signals) >= 1
