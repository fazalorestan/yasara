from fastapi import APIRouter
from app.v52_alpha_in_process_backend_runner.service import in_process_backend_runner_facade_v52_alpha as _service
router=APIRouter(prefix='/v5-2-alpha/in-process-backend',tags=['v5.2-alpha-in-process-backend'])
@router.get('/summary')
async def summary(): return _service.summary()
@router.get('/report')
async def report(): return _service.report()
@router.get('/readiness')
async def readiness(): return _service.readiness()
@router.get('/contract')
async def contract(): return _service.contract()
