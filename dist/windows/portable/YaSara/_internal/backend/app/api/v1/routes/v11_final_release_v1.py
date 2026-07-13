from fastapi import APIRouter
from app.v11_final_release.phase12_summary import V11Phase12SummaryBuilder
from app.v11_final_release.service import FinalReleaseServiceV11

router = APIRouter(prefix="/v1-1/final-release", tags=["v1.1-final-release"])

_service = FinalReleaseServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase12SummaryBuilder().build()


@router.get("/manifest")
async def manifest():
    return _service.manifest()


@router.get("/package-plan")
async def package_plan():
    return _service.package_plan()
