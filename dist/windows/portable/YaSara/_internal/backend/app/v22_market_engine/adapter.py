from time import time
from app.v22_market_engine.models import MarketTickV22, OhlcCandleV22

class DemoExchangeAdapterV22:
    def __init__(self, exchange: str = "binance"):
        self.exchange = exchange
        self.base_prices = {"BTCUSDT": 50000.0, "ETHUSDT": 3000.0, "SOLUSDT": 150.0, "XRPUSDT": 0.62, "BNBUSDT": 610.0, "ADAUSDT": 0.42}

    def normalize_symbol(self, symbol: str) -> str:
        return symbol.upper().replace("/", "").replace("-", "")

    def get_tick(self, symbol: str) -> MarketTickV22:
        normalized = self.normalize_symbol(symbol)
        base = self.base_prices.get(normalized, 100.0)
        pulse = ((int(time()) % 17) - 8) * base * 0.0005
        return MarketTickV22(symbol=normalized, exchange=self.exchange, price=round(base + pulse, 6), spread=round(max(base * 0.0002, 0.0001), 6))

    def get_ohlc(self, symbol: str, timeframe: str = "4H", limit: int = 120):
        normalized = self.normalize_symbol(symbol)
        base = self.base_prices.get(normalized, 100.0)
        now = int(time())
        price = base
        candles = []
        for i in range(limit):
            wave = ((i % 11) - 5) * base * 0.0008
            open_price = price
            close = max(0.0001, open_price + wave)
            high = max(open_price, close) + base * 0.0012
            low = min(open_price, close) - base * 0.001
            candles.append(OhlcCandleV22(time=now - (limit - i) * 3600, open=round(open_price, 6), high=round(high, 6), low=round(low, 6), close=round(close, 6), volume=round(1000 + (i % 13) * 120, 3)))
            price = close
        return candles
