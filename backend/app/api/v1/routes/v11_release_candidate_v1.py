from fastapi import APIRouter
from app.v11_release_candidate.integration_service import V11IntegrationService
from app.v11_release_candidate.rc_summary import V11ReleaseCandidateSummaryBuilder
from app.v11_release_candidate.release_manifest import V11ReleaseManifestBuilder

router = APIRouter(prefix="/v1-1/release-candidate", tags=["v1.1-release-candidate"])


@router.get("/summary")
async def summary():
    return V11ReleaseCandidateSummaryBuilder().build()


@router.get("/integration-report")
async def integration_report():
    return V11IntegrationService().report()


@router.get("/manifest")
async def manifest():
    return V11ReleaseManifestBuilder().build()
