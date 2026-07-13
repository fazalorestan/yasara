from app.v11_strategy_runtime.context_builder import StrategyContextBuilderV11

def test_strategy_context_builder_demo():
    ctx = StrategyContextBuilderV11().demo_context("BTCUSDT")
    assert ctx.symbol == "BTCUSDT"
    assert ctx.price > 0
