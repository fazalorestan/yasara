from fastapi import APIRouter
from app.v44_backtest_benchmark.models import BacktestRequestV44, BenchmarkRequestV44
from app.v44_backtest_benchmark.service import BacktestBenchmarkEngineServiceV44

router = APIRouter(prefix="/v4-4/backtest-benchmark", tags=["v4.4-backtest-benchmark"])
_service = BacktestBenchmarkEngineServiceV44()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.post("/run")
async def run_backtest(request: BacktestRequestV44):
    return _service.run_backtest(request)


@router.post("/benchmark")
async def benchmark(request: BenchmarkRequestV44):
    return _service.benchmark(request)


@router.get("/benchmark/history")
async def benchmark_history():
    return _service.benchmark_history()
