from fastapi import APIRouter
from app.v52_alpha_native_launcher.service import native_windows_launcher_facade_v52_alpha as _service
router=APIRouter(prefix='/v5-2-alpha/native-launcher',tags=['v5.2-alpha-native-launcher'])
@router.get('/summary')
async def summary(): return _service.summary()
@router.get('/report')
async def report(): return _service.report()
@router.get('/readiness')
async def readiness(): return _service.readiness()
@router.get('/contract')
async def contract(): return _service.contract()
