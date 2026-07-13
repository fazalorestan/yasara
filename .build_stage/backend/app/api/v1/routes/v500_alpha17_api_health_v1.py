from fastapi import APIRouter
from app.v500_alpha17_api_health.service import APIHealthFacadeV500Alpha17

router = APIRouter(prefix="/v5-0-alpha-17/api-health", tags=["v5.0-alpha.17-api-health"])
_service = APIHealthFacadeV500Alpha17()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/catalog")
async def catalog():
    return _service.catalog()

@router.get("/smoke")
async def smoke():
    return _service.smoke()

@router.get("/visibility")
async def visibility():
    return _service.visibility()

@router.get("/report")
async def report():
    return _service.report()

@router.get("/readiness")
async def readiness():
    return _service.readiness()

@router.get("/contract")
async def contract():
    return _service.contract()
