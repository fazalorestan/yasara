from app.platform_core.indicators.math_runtime.safety import IndicatorMathSafetyValidator

def test_v500_alpha6_safety():
    v = IndicatorMathSafetyValidator()
    assert v.validate_number(1.2)["valid"] is True
    assert v.validate_number(float("inf"))["valid"] is False
