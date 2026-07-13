from app.v24_indicator_signal.service import IndicatorSignalServiceV24

def test_indicator_snapshot():
    snap = IndicatorSignalServiceV24().snapshot("BTCUSDT", "binance", "4H")
    assert snap.symbol == "BTCUSDT"
    assert snap.ema_fast > 0
    assert 0 <= snap.rsi <= 100
    assert snap.signal in ["bullish", "bearish", "neutral", "volatile"]
