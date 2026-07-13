from app.v11_market_data.cache import MarketCacheV11
from app.v11_market_data.event_bus import MarketEventBusV11
from app.v11_market_data.health import MarketHealthMonitorV11
from app.v11_market_data.models import MarketSnapshotV11, SubscriptionRequestV11
from app.v11_market_data.rate_limit import RateLimitManagerV11
from app.v11_market_data.rest_fallback import RestFallbackProviderV11
from app.v11_market_data.subscriptions import SubscriptionManagerV11
from app.v11_market_data.ws_manager import WebSocketManagerV11


class MarketDataEngineV11:
    def __init__(self):
        self.cache = MarketCacheV11()
        self.event_bus = MarketEventBusV11()
        self.health = MarketHealthMonitorV11()
        self.subscriptions = SubscriptionManagerV11()
        self.rate_limits = RateLimitManagerV11()
        self.rest_fallback = RestFallbackProviderV11()
        self.ws = WebSocketManagerV11(self.health)

    def start_exchange(self, exchange: str) -> None:
        self.ws.connect(exchange)

    def subscribe(self, request: SubscriptionRequestV11):
        self.start_exchange(request.exchange)
        return self.subscriptions.subscribe(request)

    def ingest_synthetic_ticker(self, exchange: str, symbol: str, last_price: float = 100.0):
        ticker = self.rest_fallback.synthetic_ticker(exchange, symbol, last_price)
        item = self.cache.update_ticker(ticker)
        self.event_bus.ticker_updated(exchange.lower(), ticker.normalized_symbol, item.model_dump())
        return item

    def snapshot(self) -> MarketSnapshotV11:
        return self.cache.snapshot()

    def status(self) -> dict:
        return {
            "ready": self.health.is_ready(),
            "subscriptions": [s.model_dump() for s in self.subscriptions.list()],
            "health": [h.model_dump() for h in self.health.all()],
            "events": self.event_bus.count(),
            "snapshot_count": self.snapshot().count,
        }
