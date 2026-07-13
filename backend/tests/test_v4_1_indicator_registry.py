from app.v41_indicator_engine.registry import ModularIndicatorRegistryV41

def test_v41_registry():
    r = ModularIndicatorRegistryV41()
    names = r.names()
    assert "ema" in names
    assert "parabolic_sar" in names
    assert len(names) >= 16
