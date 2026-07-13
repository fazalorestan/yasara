from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.portfolio_v1.application.service import PortfolioIntelligenceServiceV1, get_portfolio_intelligence_service_v1
from app.portfolio_v1.domain.models import PortfolioSnapshot

router = APIRouter(prefix="/portfolio-v1", tags=["portfolio-v1"])


class PortfolioAnalysisRequest(BaseModel):
    snapshot: PortfolioSnapshot
    price_returns: dict[str, list[float]] | None = None
    targets: dict[str, float] | None = None


@router.post("/analyze")
async def analyze_portfolio(
    payload: PortfolioAnalysisRequest,
    service: PortfolioIntelligenceServiceV1 = Depends(get_portfolio_intelligence_service_v1),
):
    return await service.analyze(payload.snapshot, payload.price_returns, payload.targets)
