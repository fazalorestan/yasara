from fastapi import APIRouter
from app.v441_yasara_indicator.service import YaSaraIndicatorServiceV441

router = APIRouter(prefix="/v4-41/yasara-indicator", tags=["v4.41-yasara-indicator"])
_service = YaSaraIndicatorServiceV441()

@router.get("/summary")
async def summary(): return _service.summary()

@router.get("/registry")
async def registry(): return _service.registry()

@router.get("/contract")
async def contract(): return _service.contract()

@router.get("/default-state")
async def default_state(): return _service.default_state()

@router.post("/normalize-signal")
async def normalize_signal(raw: dict | None = None): return _service.normalize_signal(raw)
