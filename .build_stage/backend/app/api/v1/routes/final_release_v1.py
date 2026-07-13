from fastapi import APIRouter
from app.final_release_v1.final_release_summary import FinalReleaseSummaryBuilderV1
from app.final_release_v1.final_manifest import FinalReleaseManifestBuilderV1
from app.final_release_v1.final_qa_gate import FinalQAGateBuilderV1
from app.final_release_v1.release_notes import FinalReleaseNotesBuilderV1

router = APIRouter(prefix="/final-release-v1", tags=["final-release-v1"])

@router.get("/summary")
async def summary():
    return FinalReleaseSummaryBuilderV1().build()

@router.get("/manifest")
async def manifest():
    return FinalReleaseManifestBuilderV1().build()

@router.get("/qa-gate")
async def qa_gate():
    return FinalQAGateBuilderV1().build()

@router.get("/release-notes")
async def release_notes():
    return FinalReleaseNotesBuilderV1().build()
