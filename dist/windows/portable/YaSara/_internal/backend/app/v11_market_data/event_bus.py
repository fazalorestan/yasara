from collections import defaultdict
from app.v11_market_data.models import MarketEventV11, MarketEventTypeV11


class MarketEventBusV11:
    def __init__(self):
        self._events: list[MarketEventV11] = []
        self._by_type: dict[str, list[MarketEventV11]] = defaultdict(list)

    def publish(self, event: MarketEventV11) -> None:
        self._events.append(event)
        self._by_type[event.event_type.value].append(event)

    def ticker_updated(self, exchange: str, symbol: str, payload: dict) -> MarketEventV11:
        event = MarketEventV11(
            event_type=MarketEventTypeV11.TICKER_UPDATED,
            exchange=exchange,
            symbol=symbol,
            payload=payload,
        )
        self.publish(event)
        return event

    def recent(self, limit: int = 50) -> list[MarketEventV11]:
        return self._events[-limit:]

    def count(self) -> int:
        return len(self._events)
