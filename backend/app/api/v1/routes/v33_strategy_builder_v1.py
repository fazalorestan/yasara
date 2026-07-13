from fastapi import APIRouter
from app.v33_strategy_builder.models import StrategyContextV33, StrategyDefinitionV33
from app.v33_strategy_builder.service import StrategyBuilderServiceV33

router = APIRouter(prefix="/v3-3/strategy-builder", tags=["v3.3-strategy-builder"])
_service = StrategyBuilderServiceV33()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/strategies")
async def list_strategies():
    return _service.list_strategies()


@router.post("/strategies")
async def save_strategy(strategy: StrategyDefinitionV33):
    return _service.save_strategy(strategy)


@router.get("/strategies/{strategy_id}")
async def get_strategy(strategy_id: str):
    return _service.get_strategy(strategy_id)


@router.delete("/strategies/{strategy_id}")
async def archive_strategy(strategy_id: str):
    return _service.archive_strategy(strategy_id)


@router.post("/strategies/{strategy_id}/evaluate")
async def evaluate(strategy_id: str, context: StrategyContextV33 | None = None):
    return _service.evaluate(strategy_id=strategy_id, context=context)


@router.post("/demo")
async def demo_strategy():
    return _service.demo_strategy()


@router.get("/context")
async def context(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.build_context_from_ai(symbol=symbol, exchange=exchange, timeframe=timeframe)
