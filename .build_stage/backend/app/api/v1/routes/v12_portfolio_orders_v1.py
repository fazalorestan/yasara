from fastapi import APIRouter
from app.v12_portfolio_orders.service import PortfolioOrdersServiceV12
router = APIRouter(prefix="/v1-2/portfolio-orders", tags=["v1.2-portfolio-orders"])
@router.get("/summary")
async def summary():
    return PortfolioOrdersServiceV12().summary()
