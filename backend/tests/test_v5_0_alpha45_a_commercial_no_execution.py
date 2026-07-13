from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_commercial_no_execution(): assert RuntimeCoreFacadeV500Alpha45().commercial_mode()['execution_engine_enabled'] is False
