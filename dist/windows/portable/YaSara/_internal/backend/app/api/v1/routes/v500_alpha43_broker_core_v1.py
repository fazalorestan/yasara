from fastapi import APIRouter
from app.v500_alpha43_broker_core.service import broker_core_facade_v500_alpha43 as _service

router = APIRouter(prefix="/v5-0-alpha-43/broker-core", tags=["v5.0-alpha.43-broker-core"])

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/brokers")
async def brokers(): return _service.brokers()
@router.get("/adapter-contract")
async def adapter_contract(): return _service.adapter_contract()
@router.get("/dry-connect")
async def dry_connect(): return _service.dry_connect()
@router.get("/capabilities")
async def capabilities(): return _service.capabilities()
@router.get("/safety")
async def safety(): return _service.safety()
@router.get("/report")
async def report(): return _service.report()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/contract")
async def contract(): return _service.contract()
