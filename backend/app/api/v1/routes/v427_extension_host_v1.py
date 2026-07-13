from fastapi import APIRouter
from app.v427_extension_host.service import ExtensionHostServiceV427

router = APIRouter(prefix="/v4-27/extension-host", tags=["v4.27-extension-host"])
_service = ExtensionHostServiceV427()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/load-catalog")
async def load_catalog():
    return _service.load_catalog()

@router.post("/start-all")
async def start_all():
    return _service.start_all()

@router.get("/health")
async def health():
    return _service.health()

@router.get("/startup-profile")
async def startup_profile():
    return _service.startup_profile()

@router.get("/quotas")
async def quotas():
    return _service.quotas()

@router.get("/shutdown-plan")
async def shutdown_plan(plugin: str = "market_structure_pro"):
    return _service.shutdown_plan(plugin)

@router.get("/recovery-history")
async def recovery_history():
    return _service.recovery_history()
