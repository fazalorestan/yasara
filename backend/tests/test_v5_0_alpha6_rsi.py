from app.platform_core.indicators.math_runtime.rsi import RSIMath

def test_v500_alpha6_rsi():
    r = RSIMath().rsi([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 14)
    assert r == 100.0
