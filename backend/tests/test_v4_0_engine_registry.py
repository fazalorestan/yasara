from app.v40_market_context.registry import EngineRegistryV40

def test_v40_registry():
    r = EngineRegistryV40().list()
    assert r["ready"] is True
    assert r["engines"]["autotrade_gate"]["commercial_included"] is False
