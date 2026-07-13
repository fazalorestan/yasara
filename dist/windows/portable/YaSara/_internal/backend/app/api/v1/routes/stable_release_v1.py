from fastapi import APIRouter
from app.stable_release_v1.stable_manifest import StableReleaseManifestBuilderV1
from app.stable_release_v1.stable_summary import StableReleaseSummaryBuilderV1
from app.stable_release_v1.stable_validation import StableValidationBuilderV1
from app.stable_release_v1.install_guide import StableInstallGuideBuilderV1

router = APIRouter(prefix="/stable-release-v1", tags=["stable-release-v1"])

@router.get("/summary")
async def summary():
    return StableReleaseSummaryBuilderV1().build()

@router.get("/manifest")
async def manifest():
    return StableReleaseManifestBuilderV1().build()

@router.get("/validation")
async def validation():
    return StableValidationBuilderV1().build()

@router.get("/install-guide")
async def install_guide():
    return StableInstallGuideBuilderV1().build()
