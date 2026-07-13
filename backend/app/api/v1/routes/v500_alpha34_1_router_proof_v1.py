from fastapi import APIRouter
from app.v500_alpha34_1_router_proof.service import RouterProofFacadeV500Alpha341

router = APIRouter(prefix="/v5-0-alpha-34-1/router-proof", tags=["v5.0-alpha.34.1-router-proof"])
_service = RouterProofFacadeV500Alpha341()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/readiness")
async def readiness():
    return _service.readiness()

@router.get("/contract")
async def contract():
    return _service.contract()
