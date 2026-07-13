from fastapi import APIRouter
from app.v434_observability.service import svc
router=APIRouter(prefix='/v4-34/observability')
@router.get('/summary')
async def a(): return svc.summary()
@router.get('/metrics')
async def b(): return svc.metrics()
