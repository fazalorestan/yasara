from fastapi import APIRouter
from app.v20_final_release.service import V20FinalReleaseService

router = APIRouter(prefix="/v2/final-release", tags=["v2-final-release"])

@router.get("/summary")
async def summary():
    return V20FinalReleaseService().summary()

@router.get("/checklist")
async def checklist():
    return V20FinalReleaseService().checklist()
