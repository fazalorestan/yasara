from app.v500_alpha43_broker_monitoring.service import BrokerMonitoringFacadeV500Alpha43

def test_v500_alpha43_d_contract_block(): assert BrokerMonitoringFacadeV500Alpha43().contract()['execution_allowed'] is False
