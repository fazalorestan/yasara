from sqlalchemy.ext.asyncio import AsyncSession
from app.decision_v1.engine.decision_engine import DecisionEngineV1
from app.decision_v1.engine.ranking import DecisionRankingEngineV1
from app.intelligence_v1.application.service import market_intelligence_service_v1
from app.market_data.domain.models import ExchangeCode

class DecisionServiceV1:
    def __init__(self):
        self.engine = DecisionEngineV1()
        self.ranking = DecisionRankingEngineV1()

    async def decide_live(self, exchange: ExchangeCode, symbol: str, timeframes: list[str], limit: int = 250):
        report = await market_intelligence_service_v1.analyze_live(exchange, symbol, timeframes, limit)
        return self.engine.decide(report)

    async def decide_stored(self, session: AsyncSession, exchange: ExchangeCode, symbol: str, timeframes: list[str], limit: int = 250):
        report = await market_intelligence_service_v1.analyze_stored(session, exchange, symbol, timeframes, limit)
        return self.engine.decide(report)

    async def rank_live(self, exchange: ExchangeCode, symbols: list[str], timeframes: list[str], limit: int = 250):
        decisions = []
        for symbol in symbols:
            decisions.append(await self.decide_live(exchange, symbol, timeframes, limit))
        return self.ranking.rank(decisions)

decision_service_v1 = DecisionServiceV1()
