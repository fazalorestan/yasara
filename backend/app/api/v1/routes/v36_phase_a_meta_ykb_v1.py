from fastapi import APIRouter
from app.v36_phase_a_meta_ykb.models import TechnicalDebtItemV36, YKBEntryV36
from app.v36_phase_a_meta_ykb.service import PhaseAMetaYKBServiceV36

router = APIRouter(prefix="/v3-6/phase-a-meta-ykb", tags=["v3.6-phase-a-meta-ykb"])
_service = PhaseAMetaYKBServiceV36()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/health")
async def health():
    return _service.health_score()


@router.get("/ykb/status")
async def ykb_status():
    return _service.ykb_status()


@router.get("/ykb/entries")
async def list_ykb():
    return _service.list_ykb()


@router.post("/ykb/entries")
async def add_ykb(entry: YKBEntryV36):
    return _service.add_ykb(entry)


@router.get("/registry/status")
async def registry_status():
    return _service.registry_status()


@router.get("/dependency/status")
async def dependency_status():
    return _service.dependency_status()


@router.get("/data-flow/status")
async def data_flow_status():
    return _service.data_flow_status()


@router.get("/technical-debt/status")
async def technical_debt_status():
    return _service.technical_debt_status()


@router.post("/technical-debt/items")
async def add_technical_debt(item: TechnicalDebtItemV36):
    return _service.add_technical_debt(item)


@router.get("/recommendations")
async def recommendations():
    return _service.recommendations()
