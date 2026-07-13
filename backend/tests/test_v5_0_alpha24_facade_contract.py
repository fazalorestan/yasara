from app.v500_alpha24_runtime_api_smoke.service import RuntimeAPISmokeFacadeV500Alpha24

def test_v500_alpha24_facade_contract(): assert RuntimeAPISmokeFacadeV500Alpha24().contract()['execution_allowed'] is False
