from app.v500_alpha41_strategy_simulation.service import StrategySimulationFacadeV500Alpha41

def test_v500_alpha41_d_contract_block(): assert StrategySimulationFacadeV500Alpha41().contract()['execution_allowed'] is False
