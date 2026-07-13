from fastapi import APIRouter
from app.final_integration_v1.phase1_summary import FinalIntegrationPhase1SummaryBuilderV1
from app.final_integration_v1.final_release_tree import FinalReleaseTreeBuilderV1
from app.final_integration_v1.module_merge_map import ModuleMergeMapBuilderV1
from app.final_integration_v1.final_docs_map import FinalDocsMapBuilderV1

router = APIRouter(prefix="/final-integration-v1", tags=["final-integration-v1"])

@router.get("/summary")
async def summary():
    return FinalIntegrationPhase1SummaryBuilderV1().build()

@router.get("/merge-map")
async def merge_map():
    return ModuleMergeMapBuilderV1().build()

@router.get("/release-tree")
async def release_tree():
    return FinalReleaseTreeBuilderV1().build()

@router.get("/docs-map")
async def docs_map():
    return FinalDocsMapBuilderV1().build()
