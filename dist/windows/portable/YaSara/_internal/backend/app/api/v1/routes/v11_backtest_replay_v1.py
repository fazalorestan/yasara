from fastapi import APIRouter
from app.v11_backtest_replay.phase10_summary import V11Phase10SummaryBuilder
from app.v11_backtest_replay.service import BacktestReplayServiceV11

router = APIRouter(prefix="/v1-1/backtest-replay", tags=["v1.1-backtest-replay"])

_service = BacktestReplayServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase10SummaryBuilder().build()


@router.get("/demo-dataset")
async def demo_dataset(symbol: str = "BTCUSDT"):
    return _service.demo_dataset(symbol)


@router.get("/run-demo")
async def run_demo(symbol: str = "BTCUSDT"):
    return _service.run_demo(symbol)


@router.get("/summary-payload")
async def summary_payload():
    return _service.summary_payload()
