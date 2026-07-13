from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_personal_execution(): assert RuntimeCoreFacadeV500Alpha45().personal_mode()['execution_engine_enabled'] is True
