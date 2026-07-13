from app.platform_core.exchanges.models import ExchangeMetadata

class ExchangeMetadataRegistry:
    def __init__(self):
        self._items = {}

    def seed_defaults(self):
        if not self._items:
            global_exchanges = ["binance", "bybit", "okx", "kucoin", "gate", "mexc", "bitget", "bingx", "bitunix", "toobit", "lbank"]
            iran_exchanges = ["nobitex", "wallex", "tabdeal", "ramzinex", "exir", "bitpin", "ompfinex"]
            for ex in global_exchanges:
                self._items[ex] = ExchangeMetadata(
                    exchange_id=ex,
                    base_url=f"https://api.{ex}.com",
                    websocket_url=f"wss://stream.{ex}.com",
                    country="global",
                )
            for ex in iran_exchanges:
                self._items[ex] = ExchangeMetadata(
                    exchange_id=ex,
                    base_url=f"https://api.{ex}.ir",
                    websocket_url="",
                    country="iran",
                    rate_limit_per_minute=300,
                )
        return {k: v.__dict__ for k, v in self._items.items()}

    def get(self, exchange_id: str):
        self.seed_defaults()
        item = self._items.get(exchange_id.lower())
        return item.__dict__ if item else None

exchange_metadata_registry = ExchangeMetadataRegistry()
