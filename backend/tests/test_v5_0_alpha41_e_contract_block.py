from app.v500_alpha41_strategy_enterprise.service import StrategyEnterpriseFacadeV500Alpha41

def test_v500_alpha41_e_contract_block(): assert StrategyEnterpriseFacadeV500Alpha41().contract()['execution_allowed'] is False
