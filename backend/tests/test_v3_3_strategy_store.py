from app.v33_strategy_builder.models import StrategyDefinitionV33
from app.v33_strategy_builder.store import StrategyStoreV33

def test_v33_store():
    store = StrategyStoreV33()
    item = store.save(StrategyDefinitionV33(strategy_id="test-store", name="Test Store"))
    assert item.live_trading_enabled is False
    assert store.get("test-store").strategy_id == "test-store"
