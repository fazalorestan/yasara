from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.market_data.domain.models import ExchangeCode
from app.risk_v1.application.service import risk_intelligence_service_v1
from app.risk_v1.domain.models import AccountSnapshot, ExistingExposure, RiskLimits, RiskProfile

router = APIRouter(prefix="/risk-v1", tags=["risk-v1"])

class RiskAssessmentRequest(BaseModel):
    account: AccountSnapshot
    profile: RiskProfile = RiskProfile.BALANCED
    existing_exposure: list[ExistingExposure] = Field(default_factory=list)
    limits: RiskLimits | None = None
    timeframes: list[str] = ["15m", "1h", "4h"]
    limit: int = 250

@router.post("/{exchange}/live/{symbol:path}")
async def assess_live(exchange: ExchangeCode, symbol: str, payload: RiskAssessmentRequest):
    return await risk_intelligence_service_v1.assess_live(
        exchange=exchange,
        symbol=symbol,
        account=payload.account,
        profile=payload.profile,
        existing_exposure=payload.existing_exposure,
        timeframes=payload.timeframes,
        limit=payload.limit,
        limits=payload.limits,
    )

@router.post("/{exchange}/stored/{symbol:path}")
async def assess_stored(
    exchange: ExchangeCode,
    symbol: str,
    payload: RiskAssessmentRequest,
    session: AsyncSession = Depends(get_db_session),
):
    return await risk_intelligence_service_v1.assess_stored(
        session=session,
        exchange=exchange,
        symbol=symbol,
        account=payload.account,
        profile=payload.profile,
        existing_exposure=payload.existing_exposure,
        timeframes=payload.timeframes,
        limit=payload.limit,
        limits=payload.limits,
    )
