from pydantic import BaseModel, Field
from app.v11_market_data.models import SubscriptionRequestV11
from app.v11_market_data.symbol_registry import SymbolRegistryV11


class SubscriptionStateV11(BaseModel):
    exchange: str
    symbols: list[str] = Field(default_factory=list)
    channels: list[str] = Field(default_factory=list)


class SubscriptionManagerV11:
    def __init__(self):
        self.registry = SymbolRegistryV11()
        self._subscriptions: dict[str, SubscriptionStateV11] = {}

    def subscribe(self, request: SubscriptionRequestV11) -> SubscriptionStateV11:
        key = request.exchange.lower()
        normalized = [self.registry.normalize(symbol) for symbol in request.symbols]
        state = self._subscriptions.get(key) or SubscriptionStateV11(exchange=key)
        state.symbols = sorted(set(state.symbols + normalized))
        state.channels = sorted(set(state.channels + request.channels))
        self._subscriptions[key] = state
        return state

    def list(self) -> list[SubscriptionStateV11]:
        return list(self._subscriptions.values())
