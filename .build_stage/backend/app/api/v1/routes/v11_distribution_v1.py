from fastapi import APIRouter
from app.v11_distribution.phase13_summary import V11FinalDistributionSummaryBuilder
from app.v11_distribution.service import FinalDistributionServiceV11

router = APIRouter(prefix="/v1-1/distribution", tags=["v1.1-distribution"])

_service = FinalDistributionServiceV11()


@router.get("/summary")
async def summary():
    return V11FinalDistributionSummaryBuilder().build()


@router.get("/outputs")
async def outputs():
    return _service.summary()
