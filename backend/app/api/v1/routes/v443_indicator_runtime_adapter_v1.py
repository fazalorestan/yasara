from fastapi import APIRouter
from app.v443_indicator_runtime_adapter.service import IndicatorRuntimeAdapterServiceV443

router = APIRouter(prefix="/v4-43/indicator-runtime-adapter", tags=["v4.43-indicator-runtime-adapter"])
_service = IndicatorRuntimeAdapterServiceV443()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/sample-input")
async def sample_input():
    return _service.sample_input()

@router.get("/run-sample")
async def run_sample():
    return _service.run_sample()

@router.get("/runtime-contract")
async def runtime_contract():
    return _service.runtime_contract()
