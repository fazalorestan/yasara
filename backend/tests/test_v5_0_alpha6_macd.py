from app.platform_core.indicators.math_runtime.macd import MACDMath

def test_v500_alpha6_macd():
    result = MACDMath().macd([float(i) for i in range(1, 60)])
    assert result is not None
    assert "macd" in result
