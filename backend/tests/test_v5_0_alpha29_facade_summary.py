from app.v500_alpha29_backtest_engine.service import BacktestEngineFacadeV500Alpha29

def test_v500_alpha29_facade_summary(): assert BacktestEngineFacadeV500Alpha29().summary().ready is True
