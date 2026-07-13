from fastapi import APIRouter
from app.v426_platform_contracts_sdk.service import PlatformContractsSDKServiceV426

router = APIRouter(prefix="/v4-26/platform-contracts-sdk", tags=["v4.26-platform-contracts-sdk"])
_service = PlatformContractsSDKServiceV426()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/standard-response")
async def standard_response():
    return _service.standard_response()

@router.get("/capabilities")
async def capabilities():
    return _service.capabilities()

@router.get("/compatibility")
async def compatibility(plugin: str = "market_structure_pro"):
    return _service.compatibility(plugin)

@router.get("/sdk-health")
async def sdk_health():
    return _service.sdk_health()

@router.post("/sdk-smoke")
async def sdk_smoke():
    return _service.sdk_smoke()
