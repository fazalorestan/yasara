import pytest
from app.market_data.infrastructure.binance_futures_adapter import BinanceFuturesAdapter

class FakeHttp:
    async def request(self, method, path, params=None):
        if path == "/fapi/v1/exchangeInfo":
            return {"symbols": [{
                "symbol": "BTCUSDT",
                "baseAsset": "BTC",
                "quoteAsset": "USDT",
                "status": "TRADING",
                "pricePrecision": 2,
                "quantityPrecision": 3,
                "filters": [
                    {"filterType": "LOT_SIZE", "stepSize": "0.001", "minQty": "0.001"},
                    {"filterType": "PRICE_FILTER", "tickSize": "0.10"},
                    {"filterType": "MIN_NOTIONAL", "notional": "5"},
                ],
            }]}
        if path == "/fapi/v1/ticker/24hr":
            return {"symbol":"BTCUSDT","lastPrice":"100","bidPrice":"99","askPrice":"101","highPrice":"110","lowPrice":"90","volume":"10","quoteVolume":"1000","priceChangePercent":"1.5"}
        raise AssertionError(path)
    async def close(self): pass

@pytest.mark.asyncio
async def test_symbols_mapping():
    adapter = BinanceFuturesAdapter()
    adapter.http = FakeHttp()
    symbols = await adapter.symbols(force_refresh=True)
    assert symbols[0].symbol == "BTC/USDT"
    assert symbols[0].tick_size == 0.1

@pytest.mark.asyncio
async def test_ticker_mapping():
    adapter = BinanceFuturesAdapter()
    adapter.http = FakeHttp()
    ticker = await adapter.ticker("BTC/USDT")
    assert ticker.symbol == "BTC/USDT"
    assert ticker.last_price == 100
