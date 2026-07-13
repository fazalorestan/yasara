from app.v11_strategy_runtime.service import StrategyRuntimeServiceV11

def test_strategy_runtime_service_demo():
    signal = StrategyRuntimeServiceV11().demo()
    assert signal.symbol == "BTCUSDT"
    assert signal.action.value in {"buy", "sell", "hold", "block"}
