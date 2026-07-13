from time import time
from app.v23_exchange_connector.service import ExchangeConnectorServiceV23
from app.v31_live_exchange.models import LiveExchangeSummaryV31, LiveSubscriptionV31


class LiveExchangeServiceV31:
    def __init__(self):
        self.exchange_connector = ExchangeConnectorServiceV23()
        self.subscriptions = {}

    def summary(self):
        return LiveExchangeSummaryV31()

    def supported_exchanges(self):
        return {
            "ready": True,
            "exchanges": [
                {"name": "binance", "websocket_ready": True, "status": "foundation_ready"},
                {"name": "bitunix", "websocket_ready": True, "status": "foundation_ready"},
                {"name": "toobit", "websocket_ready": True, "status": "foundation_ready"},
            ],
            "live_trading_enabled": False,
        }

    def subscribe(self, sub: LiveSubscriptionV31):
        key = f"{sub.exchange}:{sub.symbol}:{sub.timeframe}"
        self.subscriptions[key] = sub.model_dump()
        return {
            "ready": True,
            "subscribed": True,
            "key": key,
            "subscription": self.subscriptions[key],
            "live_trading_enabled": False,
        }

    def unsubscribe(self, exchange: str, symbol: str, timeframe: str = "1m"):
        key = f"{exchange}:{symbol}:{timeframe}"
        existed = key in self.subscriptions
        self.subscriptions.pop(key, None)
        return {
            "ready": True,
            "unsubscribed": existed,
            "key": key,
            "live_trading_enabled": False,
        }

    def live_tick(self, symbol: str = "BTCUSDT", exchange: str = "binance"):
        quote = self.exchange_connector.quote(symbol=symbol, exchange=exchange)
        return {
            "ready": True,
            "exchange": exchange,
            "symbol": symbol.upper(),
            "ts": int(time()),
            "price": quote["last"],
            "bid": quote["bid"],
            "ask": quote["ask"],
            "spread": quote["spread"],
            "source": "v31_live_tick_stream_foundation",
            "live_trading_enabled": False,
        }

    def live_orderbook(self, symbol: str = "BTCUSDT", exchange: str = "binance"):
        orderbook = self.exchange_connector.orderbook(symbol=symbol, exchange=exchange)
        orderbook["ts"] = int(time())
        orderbook["source"] = "v31_live_orderbook_stream_foundation"
        orderbook["live_trading_enabled"] = False
        return orderbook

    def live_candles(self, symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m", limit: int = 100):
        data = self.exchange_connector.ohlc_live_ready(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=limit)
        data["ts"] = int(time())
        data["source"] = "v31_live_candle_stream_foundation"
        data["live_trading_enabled"] = False
        return data

    def realtime_status(self):
        return {
            "ready": True,
            "subscriptions_count": len(self.subscriptions),
            "subscriptions": list(self.subscriptions.values()),
            "channels": ["ticker", "orderbook", "candles"],
            "websocket_foundation_ready": True,
            "live_trading_enabled": False,
        }
