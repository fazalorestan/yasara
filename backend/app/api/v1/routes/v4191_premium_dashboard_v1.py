from fastapi import APIRouter
from app.v4191_premium_dashboard.models import PremiumDashboardSummaryV4191

router = APIRouter(prefix="/v4-19-1/premium-dashboard", tags=["v4.19.1-premium-dashboard"])

@router.get("/summary")
async def summary():
    return PremiumDashboardSummaryV4191()
