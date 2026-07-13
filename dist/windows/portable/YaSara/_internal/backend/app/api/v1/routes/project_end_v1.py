from fastapi import APIRouter
from app.project_end_v1.end_marker import ProjectEndMarkerBuilderV1
from app.project_end_v1.final_end_summary import FinalEndSummaryBuilderV1

router = APIRouter(prefix="/project-end-v1", tags=["project-end-v1"])

@router.get("/marker")
async def marker():
    return ProjectEndMarkerBuilderV1().build()

@router.get("/summary")
async def summary():
    return FinalEndSummaryBuilderV1().build()
