from pydantic import BaseModel
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.registry import exchange_registry_v1
from app.multi_exchange_v1.symbol_registry import symbol_registry_v1

class ExchangeRouteDecisionV1(BaseModel):
    selected_exchange: SupportedExchange
    symbol: str
    reason: str
    available_exchanges: list[SupportedExchange]

class ExchangeRouterEngineV1:
    def available_for_symbol(self, symbol: str) -> list[SupportedExchange]:
        exchanges = []
        for descriptor in exchange_registry_v1.descriptors():
            if symbol_registry_v1.get(descriptor.exchange, symbol):
                exchanges.append(descriptor.exchange)
        return exchanges

    def choose(self, symbol: str, preferred: SupportedExchange | None = None) -> ExchangeRouteDecisionV1:
        available = self.available_for_symbol(symbol)
        if not available:
            available = [d.exchange for d in exchange_registry_v1.descriptors()]
        if preferred and preferred in available:
            return ExchangeRouteDecisionV1(selected_exchange=preferred, symbol=symbol, reason="preferred_exchange_available", available_exchanges=available)
        selected = available[0]
        return ExchangeRouteDecisionV1(selected_exchange=selected, symbol=symbol, reason="default_first_available", available_exchanges=available)
