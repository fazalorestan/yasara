from app.platform_core.indicators.math_runtime.kernel import IndicatorCalculationKernel

def test_v500_alpha6_kernel():
    candles = [{"high":i+2, "low":i, "close":i+1} for i in range(80)]
    r = IndicatorCalculationKernel().calculate(candles)
    assert r["ready"] is True
    assert r["execution_allowed"] is False
