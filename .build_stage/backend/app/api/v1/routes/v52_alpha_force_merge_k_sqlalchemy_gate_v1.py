from fastapi import APIRouter
from app.v52_alpha_force_merge_k_sqlalchemy_gate.service import force_merge_k_sqlalchemy_gate_facade_v52_alpha as _service
router=APIRouter(prefix='/v5-2-alpha/force-merge-k-sqlalchemy-gate',tags=['v5.2-alpha-force-merge-k-sqlalchemy-gate'])
@router.get('/summary')
async def summary(): return _service.summary()
@router.get('/report')
async def report(): return _service.report()
@router.get('/readiness')
async def readiness(): return _service.readiness()
@router.get('/contract')
async def contract(): return _service.contract()
