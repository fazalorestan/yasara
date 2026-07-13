from fastapi import APIRouter
from app.rc1_hardening_v1.rc_validation_summary import RCHardeningSummaryBuilderV1
from app.rc1_hardening_v1.release_gate import ReleaseGateBuilderV1
from app.rc1_hardening_v1.api_contract import APIContractBuilderV1

router = APIRouter(prefix="/rc1-hardening-v1", tags=["rc1-hardening-v1"])

@router.get("/summary")
async def summary():
    return RCHardeningSummaryBuilderV1().build()

@router.get("/release-gate")
async def release_gate():
    return ReleaseGateBuilderV1().build()

@router.get("/api-contract")
async def api_contract():
    return APIContractBuilderV1().build()
