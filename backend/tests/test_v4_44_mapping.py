from app.platform_core.indicators.pine_source.mapping import PineToRuntimeMappingRegistry

def test_v444_mapping():
    m = PineToRuntimeMappingRegistry().seed_defaults()
    assert len(m) >= 5
    assert any(x["pine_section"] == "SMC" for x in m)
