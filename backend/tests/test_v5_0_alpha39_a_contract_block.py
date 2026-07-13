from app.v500_alpha39_live_data_core.service import LiveDataCoreFacadeV500Alpha39

def test_v500_alpha39_a_contract_block(): assert LiveDataCoreFacadeV500Alpha39().contract()['execution_allowed'] is False
