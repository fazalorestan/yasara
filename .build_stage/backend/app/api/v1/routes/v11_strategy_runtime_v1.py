from fastapi import APIRouter
from app.v11_strategy_runtime.models import StrategyContextV11, StrategyRuleV11
from app.v11_strategy_runtime.phase9_summary import V11Phase9SummaryBuilder
from app.v11_strategy_runtime.service import StrategyRuntimeServiceV11

router = APIRouter(prefix="/v1-1/strategy-runtime", tags=["v1.1-strategy-runtime"])

_service = StrategyRuntimeServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase9SummaryBuilder().build()


@router.post("/rules")
async def add_rule(rule: StrategyRuleV11):
    return _service.add_rule(rule)


@router.post("/evaluate")
async def evaluate(context: StrategyContextV11):
    return _service.evaluate(context)


@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()


@router.get("/demo")
async def demo():
    return StrategyRuntimeServiceV11().demo()
