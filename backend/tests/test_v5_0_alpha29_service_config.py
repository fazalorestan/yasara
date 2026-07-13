from app.platform_core.backtest_engine.service import BacktestEngineFoundationService

def test_v500_alpha29_service_config(): assert BacktestEngineFoundationService().config()['ready'] is True
