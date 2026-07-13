from app.platform_core.backtest_engine.readiness import BacktestEngineReadinessGate

def test_v500_alpha29_readiness():
    r=BacktestEngineReadinessGate().run(); assert r['ready'] is True; assert r['execution_allowed'] is False
