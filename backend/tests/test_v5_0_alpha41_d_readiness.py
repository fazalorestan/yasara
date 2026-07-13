from app.platform_core.strategy_engine.simulation_readiness import StrategySimulationReadinessGate

def test_v500_alpha41_d_readiness(): assert StrategySimulationReadinessGate().run()['ready'] is True
