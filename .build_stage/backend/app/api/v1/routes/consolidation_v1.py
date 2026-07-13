from fastapi import APIRouter
from app.consolidation_v1.project_manifest import ConsolidatedProjectManifestBuilderV1
from app.consolidation_v1.cleanup_policy import ConsolidationCleanupPolicyBuilderV1
from app.consolidation_v1.final_structure import FinalProjectStructureBuilderV1
from app.consolidation_v1.readiness import ConsolidationReadinessBuilderV1

router = APIRouter(prefix="/consolidation-v1", tags=["consolidation-v1"])

@router.get("/manifest")
async def manifest():
    return ConsolidatedProjectManifestBuilderV1().build()

@router.get("/cleanup-policy")
async def cleanup_policy():
    return ConsolidationCleanupPolicyBuilderV1().build()

@router.get("/final-structure")
async def final_structure():
    return FinalProjectStructureBuilderV1().build()

@router.get("/readiness")
async def readiness():
    return ConsolidationReadinessBuilderV1().build()
