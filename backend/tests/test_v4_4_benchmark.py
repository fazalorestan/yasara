from app.v44_backtest_benchmark.models import BenchmarkRequestV44
from app.v44_backtest_benchmark.service import BacktestBenchmarkEngineServiceV44

def test_v44_benchmark():
    data = BacktestBenchmarkEngineServiceV44().benchmark(BenchmarkRequestV44(versions=["v-test-a","v-test-b"]))
    assert data["ready"] is True
    assert "best_version" in data["benchmark"]
