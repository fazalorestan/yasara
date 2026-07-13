from app.platform_core.backtest_engine.service import BacktestEngineFoundationService

def test_v500_alpha29_service_trades(): assert BacktestEngineFoundationService().trades()['ready'] is True
