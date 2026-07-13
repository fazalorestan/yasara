from app.market_data.infrastructure.binance_normalizer import BinanceStreamNormalizer

def test_kline_normalizer():
    raw = {
        "e": "kline",
        "s": "BTCUSDT",
        "k": {
            "s": "BTCUSDT", "i": "1m", "t": 1000, "T": 60000,
            "o": "100", "h": "110", "l": "90", "c": "105",
            "v": "12", "q": "1200", "n": 20, "x": True,
        },
    }
    event = BinanceStreamNormalizer().kline_event(raw)
    assert event.symbol == "BTC/USDT"
    assert event.payload["candle"]["close"] == 105.0
    assert event.payload["candle"]["is_closed"] is True

def test_ticker_normalizer():
    raw = {"e": "24hrTicker", "s": "ETHUSDT", "c": "2000", "P": "1.2", "v": "10", "q": "20000"}
    event = BinanceStreamNormalizer().ticker_event(raw)
    assert event.symbol == "ETH/USDT"
    assert event.payload["last_price"] == 2000.0
