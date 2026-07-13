from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_no_real_broker(): assert RuntimeCoreFacadeV500Alpha45().safety()['real_broker_connection_enabled'] is False
