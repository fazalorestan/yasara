from app.v44_backtest_benchmark.service import BacktestBenchmarkEngineServiceV44

def test_v44_summary():
    s = BacktestBenchmarkEngineServiceV44().summary()
    assert s.product_progress_percent == 94
    assert s.constitution_compliant is True
