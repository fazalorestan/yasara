from app.v500_alpha45_runtime_lifecycle.service import RuntimeLifecycleFacadeV500Alpha45

def test_no_real_execution(): assert RuntimeLifecycleFacadeV500Alpha45().report()['real_execution_enabled'] is False
