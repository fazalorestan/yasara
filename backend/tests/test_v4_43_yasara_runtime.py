from app.platform_core.indicators.runtime.models import CandleInput, IndicatorRuntimeInput
from app.platform_core.indicators.runtime.yasara_runtime import YaSaraIndicatorRuntimeAdapter

def test_v443_yasara_runtime():
    candles = [CandleInput(time=i, open=100+i, high=101+i, low=99+i, close=100+i, volume=1000) for i in range(30)]
    out = YaSaraIndicatorRuntimeAdapter().run(IndicatorRuntimeInput(candles=candles))
    assert out.indicator == "yasara"
    assert out.signals[0].execution_allowed is False
