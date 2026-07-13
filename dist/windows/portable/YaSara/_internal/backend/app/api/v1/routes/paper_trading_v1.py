from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.paper_trading_v1.application.service import paper_trading_service_v1
from app.paper_trading_v1.domain.models import PaperOrderRequest

router = APIRouter(prefix="/paper-trading-v1", tags=["paper-trading-v1"])

class ResetRequest(BaseModel):
    equity: float = 10000

class ExecutePaperRequest(BaseModel):
    order: PaperOrderRequest
    market_price: float

class MarkToMarketRequest(BaseModel):
    prices: dict[str, float] = Field(default_factory=dict)

@router.post("/reset")
async def reset_paper_account(payload: ResetRequest):
    return await paper_trading_service_v1.reset(payload.equity)

@router.post("/execute")
async def execute_paper_order(payload: ExecutePaperRequest):
    return await paper_trading_service_v1.execute(payload.order, payload.market_price)

@router.post("/mark-to-market")
async def mark_to_market(payload: MarkToMarketRequest):
    return await paper_trading_service_v1.mark_to_market(payload.prices)

@router.get("/state")
async def state():
    return await paper_trading_service_v1.get_state()

@router.get("/dashboard")
async def dashboard():
    return await paper_trading_service_v1.dashboard()
