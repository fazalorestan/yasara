from app.v500_alpha43_broker_core.service import BrokerCoreFacadeV500Alpha43

def test_v500_alpha43_a_contract_block(): assert BrokerCoreFacadeV500Alpha43().contract()['execution_allowed'] is False
