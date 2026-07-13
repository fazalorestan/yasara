from fastapi import APIRouter
from app.v52_alpha_pydantic_settings_runtime_gate.service import pydantic_settings_runtime_gate_facade_v52_alpha as _service
router = APIRouter(prefix='/v5-2-alpha/pydantic-settings-runtime-gate', tags=['v5.2-alpha-pydantic-settings-runtime-gate'])
@router.get('/summary')
async def summary(): return _service.summary()
@router.get('/report')
async def report(): return _service.report()
@router.get('/readiness')
async def readiness(): return _service.readiness()
@router.get('/contract')
async def contract(): return _service.contract()
