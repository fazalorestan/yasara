from fastapi import APIRouter
from app.v500_alpha24_runtime_api_smoke.service import RuntimeAPISmokeFacadeV500Alpha24

router = APIRouter(prefix="/v5-0-alpha-24/runtime-api-smoke", tags=["v5.0-alpha.24-runtime-api-smoke"])
_service = RuntimeAPISmokeFacadeV500Alpha24()

@router.get("/summary")
async def summary(): return _service.summary()

@router.get("/catalog")
async def catalog(): return _service.catalog()

@router.get("/plan")
async def plan(): return _service.plan()

@router.get("/audit")
async def audit(): return _service.audit()

@router.get("/runner")
async def runner(): return _service.runner()

@router.get("/validate-status")
async def validate_status(): return _service.validate_status()

@router.get("/validate-payload")
async def validate_payload(): return _service.validate_payload()

@router.get("/readiness")
async def readiness(): return _service.readiness()

@router.get("/contract")
async def contract(): return _service.contract()
