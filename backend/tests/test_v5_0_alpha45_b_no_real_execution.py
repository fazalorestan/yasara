from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_no_real_execution(): assert RuntimeServicesFacadeV500Alpha45().report()['real_execution_enabled'] is False
