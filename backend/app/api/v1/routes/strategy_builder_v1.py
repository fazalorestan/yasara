from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.strategy_builder_v1.application.service import strategy_builder_service_v1
from app.strategy_builder_v1.domain.models import StrategyDefinition, StrategyEvaluationContext

router = APIRouter(prefix="/strategy-builder-v1", tags=["strategy-builder-v1"])

class EvaluateStrategyRequest(BaseModel):
    context: StrategyEvaluationContext

@router.post("/strategies")
async def create_strategy(strategy: StrategyDefinition):
    return await strategy_builder_service_v1.create(strategy)

@router.get("/strategies")
async def list_strategies():
    return await strategy_builder_service_v1.list()

@router.get("/strategies/{strategy_id}")
async def get_strategy(strategy_id: str):
    strategy = await strategy_builder_service_v1.get(strategy_id)
    if strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

@router.post("/strategies/{strategy_id}/evaluate")
async def evaluate_strategy(strategy_id: str, payload: EvaluateStrategyRequest):
    result = await strategy_builder_service_v1.evaluate(strategy_id, payload.context)
    if result is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return result

@router.delete("/strategies/{strategy_id}")
async def archive_strategy(strategy_id: str):
    result = await strategy_builder_service_v1.archive(strategy_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return result
