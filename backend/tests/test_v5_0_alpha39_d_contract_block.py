from app.v500_alpha39_live_data_cache.service import LiveDataCacheFacadeV500Alpha39

def test_v500_alpha39_d_contract_block(): assert LiveDataCacheFacadeV500Alpha39().contract()['execution_allowed'] is False
