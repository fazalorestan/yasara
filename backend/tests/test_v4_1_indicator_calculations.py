from app.v41_indicator_engine import calculations as c

def test_v41_calculations():
    candles = [{"open":i,"high":i+2,"low":i-2,"close":i+1,"volume":1000+i} for i in range(100,180)]
    values = c.closes(candles)
    assert c.ema(values,20) > 0
    assert c.sma(values,20) > 0
    assert 0 <= c.rsi(values,14) <= 100
    assert c.atr(candles,14) > 0
    assert "upper" in c.bollinger(values)
    assert c.vwap(candles) > 0
