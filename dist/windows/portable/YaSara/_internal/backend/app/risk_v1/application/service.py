from sqlalchemy.ext.asyncio import AsyncSession
from app.decision_v1.application.service import decision_service_v1
from app.market_data.domain.models import ExchangeCode
from app.risk_v1.domain.models import AccountSnapshot, ExistingExposure, RiskLimits, RiskProfile
from app.risk_v1.engine.risk_engine import RiskIntelligenceEngineV1

class RiskIntelligenceServiceV1:
    def __init__(self):
        self.engine = RiskIntelligenceEngineV1()

    async def assess_live(
        self,
        exchange: ExchangeCode,
        symbol: str,
        account: AccountSnapshot,
        profile: RiskProfile,
        existing_exposure: list[ExistingExposure],
        timeframes: list[str],
        limit: int,
        limits: RiskLimits | None = None,
    ):
        decision = await decision_service_v1.decide_live(exchange, symbol, timeframes, limit)
        return self.engine.assess(decision, account, profile, existing_exposure, limits)

    async def assess_stored(
        self,
        session: AsyncSession,
        exchange: ExchangeCode,
        symbol: str,
        account: AccountSnapshot,
        profile: RiskProfile,
        existing_exposure: list[ExistingExposure],
        timeframes: list[str],
        limit: int,
        limits: RiskLimits | None = None,
    ):
        decision = await decision_service_v1.decide_stored(session, exchange, symbol, timeframes, limit)
        return self.engine.assess(decision, account, profile, existing_exposure, limits)

risk_intelligence_service_v1 = RiskIntelligenceServiceV1()
