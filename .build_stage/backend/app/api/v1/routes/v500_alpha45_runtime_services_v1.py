from fastapi import APIRouter
from app.v500_alpha45_runtime_services.service import runtime_services_facade_v500_alpha45 as _service

router = APIRouter(prefix="/v5-0-alpha-45/runtime-services", tags=["v5.0-alpha.45-runtime-services"])

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/services")
async def services(): return _service.services()
@router.get("/dependency-graph")
async def dependency_graph(): return _service.dependency_graph()
@router.get("/startup-order")
async def startup_order(): return _service.startup_order()
@router.get("/service-health")
async def service_health(): return _service.service_health()
@router.get("/orchestration")
async def orchestration(): return _service.orchestration()
@router.get("/report")
async def report(): return _service.report()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/contract")
async def contract(): return _service.contract()
