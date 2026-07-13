from app.v500_alpha45_runtime_enterprise.service import RuntimeEnterpriseFacadeV500Alpha45

def test_no_real_broker(): assert RuntimeEnterpriseFacadeV500Alpha45().report()['real_broker_connection_enabled'] is False
