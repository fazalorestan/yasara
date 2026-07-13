from abc import ABC, abstractmethod
from app.multi_exchange_v1.domain.models import (
    ExchangeDescriptor,
    SupportedExchange,
    UnifiedOrderBook,
    UnifiedPrivateOrderRequest,
    UnifiedPrivateOrderResult,
    UnifiedTicker,
)

class BaseExchangeAdapterV1(ABC):
    exchange: SupportedExchange

    @abstractmethod
    def descriptor(self) -> ExchangeDescriptor:
        raise NotImplementedError

    @abstractmethod
    async def ticker(self, symbol: str) -> UnifiedTicker:
        raise NotImplementedError

    @abstractmethod
    async def order_book(self, symbol: str, limit: int = 20) -> UnifiedOrderBook:
        raise NotImplementedError

    @abstractmethod
    async def place_order_dry_run(self, request: UnifiedPrivateOrderRequest) -> UnifiedPrivateOrderResult:
        raise NotImplementedError
