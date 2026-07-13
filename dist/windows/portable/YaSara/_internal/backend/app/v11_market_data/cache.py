from app.v11_market_data.models import MarketSnapshotItemV11, MarketSnapshotV11, MarketTickerV11
from app.v11_market_data.symbol_registry import SymbolRegistryV11


class MarketCacheV11:
    def __init__(self):
        self.registry = SymbolRegistryV11()
        self._items: dict[tuple[str, str], MarketSnapshotItemV11] = {}

    def update_ticker(self, ticker: MarketTickerV11) -> MarketSnapshotItemV11:
        key = (ticker.exchange.lower(), ticker.normalized_symbol)
        item = MarketSnapshotItemV11(
            exchange=ticker.exchange.lower(),
            symbol=ticker.symbol,
            normalized_symbol=ticker.normalized_symbol,
            last_price=ticker.last_price,
            bid=ticker.bid,
            ask=ticker.ask,
            spread=ticker.spread,
            volume_24h=ticker.volume_24h,
            timestamp=ticker.timestamp,
        )
        self._items[key] = item
        return item

    def update_funding(self, exchange: str, symbol: str, funding_rate: float) -> MarketSnapshotItemV11:
        normalized = self.registry.normalize(symbol)
        key = (exchange.lower(), normalized)
        item = self._items.get(key) or MarketSnapshotItemV11(
            exchange=exchange.lower(),
            symbol=symbol,
            normalized_symbol=normalized,
        )
        item.funding_rate = funding_rate
        self._items[key] = item
        return item

    def update_open_interest(self, exchange: str, symbol: str, open_interest: float) -> MarketSnapshotItemV11:
        normalized = self.registry.normalize(symbol)
        key = (exchange.lower(), normalized)
        item = self._items.get(key) or MarketSnapshotItemV11(
            exchange=exchange.lower(),
            symbol=symbol,
            normalized_symbol=normalized,
        )
        item.open_interest = open_interest
        self._items[key] = item
        return item

    def get(self, exchange: str, symbol: str) -> MarketSnapshotItemV11 | None:
        return self._items.get((exchange.lower(), self.registry.normalize(symbol)))

    def snapshot(self) -> MarketSnapshotV11:
        items = list(self._items.values())
        return MarketSnapshotV11(ready=True, count=len(items), items=items)
