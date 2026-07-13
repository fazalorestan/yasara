from app.platform_core.market_data.models import OHLCV
def test_v500_alpha15_models_ohlcv():
    c = OHLCV(symbol="BTCUSDT", timeframe="1h", open_time=1, open=1, high=2, low=1, close=2, volume=10)
    assert c.high >= c.low
