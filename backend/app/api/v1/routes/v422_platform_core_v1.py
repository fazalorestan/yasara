from fastapi import APIRouter
from app.platform_core.models import PlatformCoreSummaryV422
from app.platform_core.kernel.plugin_registry import plugin_registry
from app.platform_core.kernel.health_registry import health_registry
from app.platform_core.governance.feature_flags import feature_flag_center
from app.platform_core.governance.metrics import metrics

router = APIRouter(prefix="/v4-22/platform-core", tags=["v4.22-platform-core"])

@router.get("/summary")
async def summary():
    return PlatformCoreSummaryV422()

@router.get("/plugins")
async def plugins():
    return {"ready": True, "plugins": plugin_registry.list()}

@router.get("/health")
async def health():
    return health_registry.summary()

@router.get("/feature-flags")
async def feature_flags():
    return {"ready": True, "global": feature_flag_center.list_global()}

@router.get("/metrics")
async def metrics_snapshot():
    return {"ready": True, "metrics": metrics.snapshot()}
