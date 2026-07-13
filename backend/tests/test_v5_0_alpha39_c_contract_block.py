from app.v500_alpha39_live_stream_manager.service import LiveStreamManagerFacadeV500Alpha39

def test_v500_alpha39_c_contract_block(): assert LiveStreamManagerFacadeV500Alpha39().contract()['execution_allowed'] is False
