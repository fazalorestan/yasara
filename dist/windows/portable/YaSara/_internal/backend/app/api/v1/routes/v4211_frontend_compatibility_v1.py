from fastapi import APIRouter
from app.v4211_frontend_compatibility.models import FrontendCompatibilitySummaryV4211

router = APIRouter(prefix="/v4-21-1/frontend-compatibility", tags=["v4.21.1-frontend-compatibility"])

@router.get("/summary")
async def summary():
    return FrontendCompatibilitySummaryV4211()
