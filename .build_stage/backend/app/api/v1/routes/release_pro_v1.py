from fastapi import APIRouter
from app.release_pro_v1.final_summary import FinalProfessionalSummaryBuilderV1
from app.release_pro_v1.pro_manifest import ProfessionalManifestBuilderV1
from app.release_pro_v1.health_audit import HealthAuditBuilderV1

router = APIRouter(prefix="/release-pro-v1", tags=["release-pro-v1"])

@router.get("/summary")
async def summary():
    return FinalProfessionalSummaryBuilderV1().build()

@router.get("/manifest")
async def manifest():
    return ProfessionalManifestBuilderV1().build()

@router.get("/health-audit")
async def health_audit():
    return HealthAuditBuilderV1().build()
