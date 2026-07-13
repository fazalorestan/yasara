from fastapi import APIRouter
from app.platform_core.paths import ensure_platform_dirs

router = APIRouter(prefix="/v4-23-1/path-resolver", tags=["v4.23.1-path-resolver"])

@router.get("/summary")
async def summary():
    return {
        "ready": True,
        "phase": "v4_23_1_platform_path_resolver_manifest_loader_fix",
        "scope": "infrastructure_fix",
        "paths": ensure_platform_dirs(),
        "no_new_trading_features": True,
        "backward_compatible": True,
        "safety": "infrastructure_only_no_real_execution",
    }
