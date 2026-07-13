from fastapi import APIRouter
from app.v500_alpha37_broker_core.service import broker_core_facade_v500_alpha37 as _service

router = APIRouter(prefix="/v5-0-alpha-37/broker-core", tags=["v5.0-alpha.37-broker-core"])

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/contract")
async def contract(): return _service.contract()
@router.get("/brokers")
async def brokers(): return _service.brokers()
@router.get("/default-broker")
async def default_broker(): return _service.default_broker()
@router.get("/capabilities")
async def capabilities(): return _service.capabilities()
@router.get("/health")
async def health(): return _service.health()
@router.get("/safety")
async def safety(): return _service.safety()
@router.get("/status")
async def status(): return _service.status()
@router.get("/readiness")
async def readiness(): return _service.readiness()
