from fastapi import APIRouter
from app.v500_alpha6_indicator_math.service import IndicatorMathFacadeV500Alpha6

router = APIRouter(prefix="/v5-0-alpha-6/indicator-math", tags=["v5.0-alpha.6-indicator-math"])
_service = IndicatorMathFacadeV500Alpha6()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/calculate-sample")
async def calculate_sample():
    return _service.calculate_sample()

@router.get("/contract")
async def contract():
    return _service.contract()
