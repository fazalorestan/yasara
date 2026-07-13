from app.v11_strategy_runtime.strategy_store import StrategyStoreV11

def test_strategy_store_seed_demo():
    store = StrategyStoreV11()
    rules = store.seed_demo_rules()
    assert len(rules) >= 2
