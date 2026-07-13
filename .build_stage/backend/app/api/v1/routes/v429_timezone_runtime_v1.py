from fastapi import APIRouter
from app.v429_timezone_runtime.service import TimezoneRuntimeServiceV429

router = APIRouter(prefix="/v4-29/timezone-runtime", tags=["v4.29-timezone-runtime"])
_service = TimezoneRuntimeServiceV429()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/now")
async def now():
    return _service.now()

@router.post("/smoke")
async def smoke():
    return _service.smoke()
