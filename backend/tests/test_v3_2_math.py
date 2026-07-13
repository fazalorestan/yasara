from app.v32_advanced_ai_indicators.math import atr, bollinger, ema, ichimoku, macd, rsi, supertrend

def test_v32_math():
    values = list(range(1, 80))
    candles = [{"open":x, "high":x+2, "low":x-2, "close":x+1, "volume":1000} for x in values]
    assert ema(values, 20) > 0
    assert 0 <= rsi(values, 14) <= 100
    assert isinstance(macd(values)[0], float)
    assert atr(candles, 14) > 0
    assert bollinger(values)["upper"] >= bollinger(values)["lower"]
    assert supertrend(candles)["trend"] in ["bullish", "bearish"]
    assert ichimoku(candles)["cloud"] in ["bullish", "bearish", "neutral"]
