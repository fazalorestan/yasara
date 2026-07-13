from app.platform_core.backtest_engine.signal_simulator import BacktestSignalSimulator

def test_v500_alpha29_signals():
    r=BacktestSignalSimulator().generate([{'close':1},{'close':2}]); assert len(r['signals']) == 2
