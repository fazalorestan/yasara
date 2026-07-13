from fastapi import APIRouter
from app.final_release_engineering_v1.release_engineering_summary import ReleaseEngineeringSummaryBuilderV1
from app.final_release_engineering_v1.artifact_manifest import ArtifactManifestBuilderV1
from app.final_release_engineering_v1.release_export_gate import ReleaseExportGateBuilderV1

router = APIRouter(prefix="/final-release-engineering-v1", tags=["final-release-engineering-v1"])

@router.get("/summary")
async def summary():
    return ReleaseEngineeringSummaryBuilderV1().build()

@router.get("/artifacts")
async def artifacts():
    return ArtifactManifestBuilderV1().build()

@router.get("/export-gate")
async def export_gate():
    return ReleaseExportGateBuilderV1().build()
