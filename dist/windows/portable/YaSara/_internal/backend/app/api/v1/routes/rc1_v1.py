from fastapi import APIRouter
from app.rc1_v1.rc_summary import RC1SummaryBuilderV1
from app.rc1_v1.rc_manifest import RCManifestBuilderV1
from app.rc1_v1.security_gate import SecurityGateBuilderV1

router = APIRouter(prefix="/rc1-v1", tags=["rc1-v1"])

@router.get("/summary")
async def summary():
    return RC1SummaryBuilderV1().build()

@router.get("/manifest")
async def manifest():
    return RCManifestBuilderV1().build()

@router.get("/security-gate")
async def security_gate():
    return SecurityGateBuilderV1().build()
