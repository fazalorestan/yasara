from fastapi import APIRouter
from app.v361_phase_a_guardrails.models import FeatureValidationRequestV361, YKBSearchRequestV361
from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

router = APIRouter(prefix="/v3-6-1/phase-a-guardrails", tags=["v3.6.1-phase-a-guardrails"])
_service = PhaseAGuardrailsServiceV361()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/registry/validate")
async def registry_validation():
    return _service.registry_validation()


@router.get("/dependency/validate")
async def dependency_validation():
    return _service.dependency_validation()


@router.get("/feature-flags/status")
async def feature_flags_status():
    return _service.feature_flags_status()


@router.post("/feature/validate")
async def validate_feature(request: FeatureValidationRequestV361):
    return _service.validate_new_feature(request)


@router.post("/ykb/search")
async def ykb_search(request: YKBSearchRequestV361):
    return _service.ykb_search(request)


@router.get("/ykb/stats")
async def ykb_stats():
    return _service.ykb_stats()


@router.get("/health")
async def health():
    return _service.health_aggregate()


@router.get("/recommendations")
async def recommendations():
    return _service.recommendations()
