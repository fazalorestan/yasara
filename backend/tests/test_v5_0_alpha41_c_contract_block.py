from app.v500_alpha41_strategy_allocation.service import StrategyAllocationFacadeV500Alpha41

def test_v500_alpha41_c_contract_block(): assert StrategyAllocationFacadeV500Alpha41().contract()['execution_allowed'] is False
