from fastapi import APIRouter
from app.v500_alpha42_execution_core.service import execution_core_facade_v500_alpha42 as _service

router = APIRouter(prefix="/v5-0-alpha-42/execution-core", tags=["v5.0-alpha.42-execution-core"])

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/core-status")
async def core_status(): return _service.core_status()
@router.get("/order-contract")
async def order_contract(): return _service.order_contract()
@router.get("/order-intent")
async def order_intent(): return _service.order_intent()
@router.get("/dry-run")
async def dry_run(): return _service.dry_run()
@router.get("/safety")
async def safety(): return _service.safety()
@router.get("/report")
async def report(): return _service.report()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/contract")
async def contract(): return _service.contract()
