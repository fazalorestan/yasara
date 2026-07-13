from app.v500_alpha39_live_data_enterprise.service import LiveDataEnterpriseFacadeV500Alpha39

def test_v500_alpha39_e_contract_block(): assert LiveDataEnterpriseFacadeV500Alpha39().contract()['execution_allowed'] is False
