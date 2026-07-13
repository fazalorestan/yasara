from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_commercial_no_execution(): assert RuntimeServicesFacadeV500Alpha45().report()['commercial_execution_engine_enabled'] is False
