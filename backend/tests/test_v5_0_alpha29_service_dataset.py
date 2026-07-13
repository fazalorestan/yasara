from app.platform_core.backtest_engine.service import BacktestEngineFoundationService

def test_v500_alpha29_service_dataset(): assert BacktestEngineFoundationService().dataset()['real_market_data'] is False
