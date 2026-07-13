from app.v500_alpha41_strategy_scoring.service import StrategyScoringFacadeV500Alpha41

def test_v500_alpha41_b_contract_block(): assert StrategyScoringFacadeV500Alpha41().contract()['execution_allowed'] is False
