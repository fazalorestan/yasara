from app.platform_core.strategy_engine.simulation_report import StrategySimulationReport

def test_v500_alpha41_d_report(): assert StrategySimulationReport().report()['ready'] is True
