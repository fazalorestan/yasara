from app.platform_core.backtest_engine.service import BacktestEngineFoundationService

def test_v500_alpha29_service_run(): assert BacktestEngineFoundationService().run()['execution_allowed'] is False
