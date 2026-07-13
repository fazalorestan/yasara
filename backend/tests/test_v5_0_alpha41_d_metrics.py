from app.platform_core.strategy_engine.result_metrics import StrategyResultMetricsService

def test_v500_alpha41_d_metrics(): assert StrategyResultMetricsService().metrics()['total_trades']==0
