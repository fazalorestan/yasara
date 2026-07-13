from app.v34_market_analysis.detectors import analyze_volume, detect_momentum, detect_range, detect_regime, detect_trend, detect_volatility

def test_v34_detectors():
    candles = [{"open":i, "high":i+2, "low":i-2, "close":i+1, "volume":100+i} for i in range(100, 170)]
    closes = [c["close"] for c in candles]
    trend = detect_trend(closes)
    range_data = detect_range(candles)
    volatility = detect_volatility(candles)
    momentum = detect_momentum(closes)
    volume = analyze_volume(candles)
    regime = detect_regime(trend, range_data, volatility, momentum)
    assert trend["trend"] in ["bullish", "bearish", "sideways", "unknown"]
    assert "is_range" in range_data
    assert volatility["volatility"] in ["low", "medium", "high", "unknown"]
    assert momentum["momentum"] in ["positive", "negative", "neutral", "unknown"]
    assert volume["volume_state"] in ["expanding", "contracting", "normal", "unknown"]
    assert regime in ["range", "trending", "volatile_momentum", "mixed"]
