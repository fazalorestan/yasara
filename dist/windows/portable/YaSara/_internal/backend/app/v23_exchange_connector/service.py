from app.v22_market_engine.service import MarketDataEngineServiceV22
from app.v23_exchange_connector.models import ExchangeCapabilityV23, ExchangeConnectorSummaryV23


class ExchangeConnectorServiceV23:
    def __init__(self):
        self.market = MarketDataEngineServiceV22()

    def summary(self):
        return ExchangeConnectorSummaryV23()

    def capabilities(self):
        return {
            "ready": True,
            "exchanges": [
                ExchangeCapabilityV23(exchange="binance"),
                ExchangeCapabilityV23(exchange="toobit"),
                ExchangeCapabilityV23(exchange="bitunix"),
            ],
            "live_trading_enabled": False,
        }

    def normalized_symbol(self, symbol: str):
        return symbol.upper().replace("/", "").replace("-", "").strip()

    def quote(self, symbol: str = "BTCUSDT", exchange: str = "binance"):
        symbol = self.normalized_symbol(symbol)
        tick = self.market.tick(symbol, exchange)
        return {
            "ready": True,
            "symbol": tick.symbol,
            "exchange": tick.exchange,
            "bid": round(tick.price - tick.spread / 2, 6),
            "ask": round(tick.price + tick.spread / 2, 6),
            "last": tick.price,
            "spread": tick.spread,
            "source": "v23_exchange_connector",
            "live_trading_enabled": False,
        }

    def ohlc_live_ready(self, symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H", limit: int = 120):
        symbol = self.normalized_symbol(symbol)
        data = self.market.ohlc(symbol, exchange, timeframe, limit)
        return {
            "ready": True,
            "symbol": data.symbol,
            "exchange": data.exchange,
            "timeframe": data.timeframe,
            "candles": [c.model_dump() for c in data.candles],
            "source": "v23_exchange_connector_ohlc",
            "live_trading_enabled": False,
        }

    def orderbook(self, symbol: str = "BTCUSDT", exchange: str = "binance"):
        quote = self.quote(symbol, exchange)
        last = quote["last"]
        spread = max(quote["spread"], 0.0001)
        asks = [{"price": round(last + spread * i, 6), "amount": round(0.1 + i * 0.07, 4)} for i in range(1, 8)]
        bids = [{"price": round(last - spread * i, 6), "amount": round(0.12 + i * 0.06, 4)} for i in range(1, 8)]
        return {
            "ready": True,
            "symbol": self.normalized_symbol(symbol),
            "exchange": exchange,
            "asks": asks,
            "bids": bids,
            "source": "v23_exchange_connector_orderbook",
            "live_trading_enabled": False,
        }
