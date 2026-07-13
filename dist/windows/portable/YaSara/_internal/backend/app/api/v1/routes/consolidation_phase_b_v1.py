from fastapi import APIRouter
from app.consolidation_v1.archive_plan import ArchivePlanBuilderV1
from app.consolidation_v1.package_manifest import FinalPackageManifestBuilderV1
from app.consolidation_v1.phase_b_readiness import ConsolidationPhaseBReadinessBuilderV1
from app.consolidation_v1.release_tree import ReleaseTreePlanBuilderV1
from app.consolidation_v1.size_report import ProjectSizeReportBuilderV1

router = APIRouter(prefix="/consolidation-phase-b-v1", tags=["consolidation-phase-b-v1"])

@router.get("/size-policy")
async def size_policy():
    return ProjectSizeReportBuilderV1().build_static_policy()

@router.get("/archive-plan")
async def archive_plan():
    return ArchivePlanBuilderV1().build()

@router.get("/package-manifest")
async def package_manifest():
    return FinalPackageManifestBuilderV1().build()

@router.get("/release-tree")
async def release_tree():
    return ReleaseTreePlanBuilderV1().build()

@router.get("/readiness")
async def readiness():
    return ConsolidationPhaseBReadinessBuilderV1().build()
