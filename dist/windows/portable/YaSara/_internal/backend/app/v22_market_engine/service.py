from app.v21_real_data.service import RealDataActivationServiceV21
from app.v22_market_engine.adapter import DemoExchangeAdapterV22
from app.v22_market_engine.models import MarketEngineSummaryV22, OhlcResponseV22

class MarketDataEngineServiceV22:
    def summary(self):
        return MarketEngineSummaryV22()

    def get_adapter(self, exchange: str):
        return DemoExchangeAdapterV22(exchange=exchange)

    def tick(self, symbol: str, exchange: str = "binance"):
        return self.get_adapter(exchange).get_tick(symbol)

    def ohlc(self, symbol: str, exchange: str = "binance", timeframe: str = "4H", limit: int = 120):
        return OhlcResponseV22(symbol=symbol.upper(), exchange=exchange, timeframe=timeframe, candles=self.get_adapter(exchange).get_ohlc(symbol, timeframe, limit))

    def snapshot(self, exchange: str = "all"):
        base = RealDataActivationServiceV21().market_snapshot(exchange)
        items = []
        for item in base["items"]:
            tick = self.tick(item["symbol"], item["exchange"])
            items.append({**item, "last_price": tick.price, "spread": tick.spread, "source": "v22_market_data_engine"})
        return {"ready": True, "exchange": exchange, "count": len(items), "items": items, "live_trading_enabled": False, "source": "v22_market_data_engine"}
