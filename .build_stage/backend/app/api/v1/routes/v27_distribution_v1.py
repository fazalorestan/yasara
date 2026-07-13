from fastapi import APIRouter
from app.v27_distribution.service import FinalDistributionServiceV27

router = APIRouter(prefix="/v2-7/distribution", tags=["v2.7-distribution"])
_service = FinalDistributionServiceV27()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/manifest")
async def manifest():
    return _service.manifest()
