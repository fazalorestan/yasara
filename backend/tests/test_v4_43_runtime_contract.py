from app.v443_indicator_runtime_adapter.service import IndicatorRuntimeAdapterServiceV443

def test_v443_runtime_contract():
    c = IndicatorRuntimeAdapterServiceV443().runtime_contract()
    assert "candles" in c["input"]
    assert "overlays" in c["output"]
