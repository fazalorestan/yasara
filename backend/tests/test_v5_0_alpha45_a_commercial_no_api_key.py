from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_commercial_no_api_key(): assert RuntimeCoreFacadeV500Alpha45().commercial_mode()['api_key_required'] is False
