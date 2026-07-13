from app.platform_core.indicators.runtime.models import CandleInput, IndicatorRuntimeInput

def test_v443_runtime_models():
    c = CandleInput(time=1, open=1, high=2, low=0.5, close=1.5, volume=100)
    i = IndicatorRuntimeInput(candles=[c])
    assert i.candles[0].close == 1.5
