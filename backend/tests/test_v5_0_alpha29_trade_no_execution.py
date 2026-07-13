from app.platform_core.backtest_engine.trade_simulator import TradeSimulationEngine

def test_v500_alpha29_trade_no_execution(): assert TradeSimulationEngine().simulate('BTCUSDT',[])['execution_allowed'] is False
