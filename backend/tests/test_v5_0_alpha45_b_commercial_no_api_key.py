from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_commercial_no_api_key(): assert RuntimeServicesFacadeV500Alpha45().report()['commercial_api_key_required'] is False
