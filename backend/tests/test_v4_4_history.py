from app.v44_backtest_benchmark.service import BacktestBenchmarkEngineServiceV44

def test_v44_history():
    data = BacktestBenchmarkEngineServiceV44().benchmark_history()
    assert data["ready"] is True
    assert "items" in data
