from fastapi import APIRouter
from app.v351_constitution_audit.service import ConstitutionAuditServiceV351

router = APIRouter(prefix="/v3-5-1/constitution-audit", tags=["v3.5.1-constitution-audit"])
_service = ConstitutionAuditServiceV351()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/health")
async def health():
    return _service.health()


@router.get("/recommendations")
async def recommendations():
    return _service.recommendations()
