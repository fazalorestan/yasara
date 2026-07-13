from fastapi import APIRouter
from app.v500_alpha43_broker_monitoring.service import broker_monitoring_facade_v500_alpha43 as _service

router = APIRouter(prefix="/v5-0-alpha-43/broker-monitoring", tags=["v5.0-alpha.43-broker-monitoring"])

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/health")
async def health(): return _service.health()
@router.get("/connection-status")
async def connection_status(): return _service.connection_status()
@router.get("/latency")
async def latency(): return _service.latency()
@router.get("/diagnostics")
async def diagnostics(): return _service.diagnostics()
@router.get("/safety")
async def safety(): return _service.safety()
@router.get("/report")
async def report(): return _service.report()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/contract")
async def contract(): return _service.contract()
