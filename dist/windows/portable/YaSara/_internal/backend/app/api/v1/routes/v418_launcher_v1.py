from fastapi import APIRouter
from app.v418_launcher.models import LauncherSummaryV418

router = APIRouter(prefix="/v4-18/launcher", tags=["v4.18-launcher"])

@router.get("/summary")
async def summary():
    return LauncherSummaryV418()
