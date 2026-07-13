from app.market_data.domain.models import ExchangeCode
from app.market_data.domain.ports import MarketDataExchangePort
from app.market_data.infrastructure.binance_futures_adapter import BinanceFuturesAdapter

class MarketDataService:
    def __init__(self):
        self._adapters: dict[ExchangeCode, MarketDataExchangePort] = {
            ExchangeCode.BINANCE_FUTURES: BinanceFuturesAdapter(),
        }

    def adapter(self, exchange: ExchangeCode) -> MarketDataExchangePort:
        if exchange not in self._adapters:
            raise ValueError(f"Unsupported exchange: {exchange}")
        return self._adapters[exchange]

    async def health(self, exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES):
        return await self.adapter(exchange).health()

    async def symbols(self, exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES, force_refresh: bool = False):
        return await self.adapter(exchange).symbols(force_refresh=force_refresh)

    async def ticker(self, symbol: str, exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES):
        return await self.adapter(exchange).ticker(symbol)

    async def candles(self, symbol: str, timeframe: str, limit: int = 500, exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES):
        return await self.adapter(exchange).candles(symbol, timeframe, limit)

    async def order_book(self, symbol: str, limit: int = 100, exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES):
        return await self.adapter(exchange).order_book(symbol, limit)

    async def funding_rate(self, symbol: str, exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES):
        return await self.adapter(exchange).funding_rate(symbol)

    async def open_interest(self, symbol: str, exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES):
        return await self.adapter(exchange).open_interest(symbol)

market_data_service = MarketDataService()
