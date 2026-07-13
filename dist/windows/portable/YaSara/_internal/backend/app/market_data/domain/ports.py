from abc import ABC, abstractmethod
from datetime import datetime
from app.market_data.domain.models import Candle, ExchangeHealth, FundingRate, MarketSymbol, OpenInterest, OrderBook, Ticker

class MarketDataExchangePort(ABC):
    @abstractmethod
    async def health(self) -> ExchangeHealth: ...

    @abstractmethod
    async def symbols(self, force_refresh: bool = False) -> list[MarketSymbol]: ...

    @abstractmethod
    async def ticker(self, symbol: str) -> Ticker: ...

    @abstractmethod
    async def candles(self, symbol: str, timeframe: str, limit: int = 500, start_time: datetime | None = None) -> list[Candle]: ...

    @abstractmethod
    async def order_book(self, symbol: str, limit: int = 100) -> OrderBook: ...

    @abstractmethod
    async def funding_rate(self, symbol: str) -> FundingRate: ...

    @abstractmethod
    async def open_interest(self, symbol: str) -> OpenInterest: ...

    @abstractmethod
    async def close(self) -> None: ...
