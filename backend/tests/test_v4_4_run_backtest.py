from app.v44_backtest_benchmark.models import BacktestRequestV44
from app.v44_backtest_benchmark.service import BacktestBenchmarkEngineServiceV44

def test_v44_run_backtest():
    data = BacktestBenchmarkEngineServiceV44().run_backtest(BacktestRequestV44(limit=80))
    assert data["ready"] is True
    assert "statistics" in data
    assert data["real_order_execution_enabled"] is False
