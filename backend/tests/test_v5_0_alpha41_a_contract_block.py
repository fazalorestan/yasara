from app.v500_alpha41_strategy_core.service import StrategyCoreFacadeV500Alpha41

def test_v500_alpha41_a_contract_block(): assert StrategyCoreFacadeV500Alpha41().contract()['execution_allowed'] is False
