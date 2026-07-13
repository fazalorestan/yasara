from app.v24_indicator_signal.math import ema, macd, rsi

def test_indicator_math():
    values = list(range(1, 40))
    assert ema(values, 12) > 0
    assert 0 <= rsi(values, 14) <= 100
    m, s = macd(values)
    assert isinstance(m, float)
    assert isinstance(s, float)
