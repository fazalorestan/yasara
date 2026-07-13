from app.platform_core.indicators.math_runtime.moving_average import MovingAverageMath

def test_v500_alpha6_moving_average():
    m = MovingAverageMath()
    assert m.sma([1,2,3], 3) == 2
    assert m.ema([1,2,3], 2) is not None
