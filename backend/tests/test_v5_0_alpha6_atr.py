from app.platform_core.indicators.math_runtime.atr import ATRMath

def test_v500_alpha6_atr():
    highs = [float(i+2) for i in range(30)]
    lows = [float(i) for i in range(30)]
    closes = [float(i+1) for i in range(30)]
    assert ATRMath().atr(highs, lows, closes, 14) is not None
