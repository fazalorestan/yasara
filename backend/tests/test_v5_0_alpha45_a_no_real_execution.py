from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_no_real_execution(): assert RuntimeCoreFacadeV500Alpha45().safety()['real_execution_enabled'] is False
