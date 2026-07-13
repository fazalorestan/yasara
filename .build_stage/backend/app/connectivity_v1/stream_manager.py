from enum import StrEnum
from pydantic import BaseModel, Field

class StreamType(StrEnum):
    TICKER = "ticker"
    TRADE = "trade"
    ORDER_BOOK = "order_book"
    KLINE = "kline"

class StreamSubscriptionV1(BaseModel):
    stream_id: str
    exchange: str
    symbol: str
    stream_type: StreamType
    active: bool = True

class MultiStreamManagerV1:
    def __init__(self):
        self.subscriptions: dict[str, StreamSubscriptionV1] = {}

    def subscribe(self, subscription: StreamSubscriptionV1) -> StreamSubscriptionV1:
        self.subscriptions[subscription.stream_id] = subscription
        return subscription

    def unsubscribe(self, stream_id: str) -> bool:
        item = self.subscriptions.get(stream_id)
        if item is None:
            return False
        item.active = False
        return True

    def active(self) -> list[StreamSubscriptionV1]:
        return [s for s in self.subscriptions.values() if s.active]
