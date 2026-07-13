from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_no_real_broker(): assert RuntimeServicesFacadeV500Alpha45().report()['real_broker_connection_enabled'] is False
