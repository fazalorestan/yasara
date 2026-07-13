from sqlalchemy.ext.asyncio import AsyncSession
from app.intelligence_v1.engine.market_intelligence import MarketIntelligenceEngineV1
from app.market_data.application.service import market_data_service
from app.market_data.application.sync_service import market_data_sync_service
from app.market_data.domain.models import ExchangeCode

class MarketIntelligenceServiceV1:
    def __init__(self):
        self.engine = MarketIntelligenceEngineV1()

    async def analyze_live(
        self,
        exchange: ExchangeCode,
        symbol: str,
        timeframes: list[str],
        limit: int = 250,
    ):
        data = {}
        for timeframe in timeframes:
            data[timeframe] = await market_data_service.candles(symbol, timeframe, limit, exchange)
        return self.engine.analyze(exchange.value, symbol, data)

    async def analyze_stored(
        self,
        session: AsyncSession,
        exchange: ExchangeCode,
        symbol: str,
        timeframes: list[str],
        limit: int = 250,
    ):
        data = {}
        for timeframe in timeframes:
            data[timeframe] = await market_data_sync_service.stored_candles(session, symbol, timeframe, limit, exchange)
        return self.engine.analyze(exchange.value, symbol, data)

market_intelligence_service_v1 = MarketIntelligenceServiceV1()
