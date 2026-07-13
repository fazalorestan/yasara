from app.intelligence_v1.engine.indicators import IndicatorCalculator

def test_sma_ema_rsi():
    calc = IndicatorCalculator()
    values = [float(i) for i in range(1, 60)]
    assert calc.sma(values, 20) is not None
    assert calc.ema(values, 20) is not None
    assert calc.rsi(values, 14) == 100.0

def test_macd():
    calc = IndicatorCalculator()
    values = [float(i) for i in range(1, 80)]
    macd, signal, hist = calc.macd(values)
    assert macd is not None
    assert signal is not None
    assert hist is not None
