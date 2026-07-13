from app.v500_alpha29_backtest_engine.service import BacktestEngineFacadeV500Alpha29

def test_v500_alpha29_facade_contract(): assert BacktestEngineFacadeV500Alpha29().contract()['execution_allowed'] is False
