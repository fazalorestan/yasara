from app.v500_alpha43_broker_order.service import BrokerOrderFacadeV500Alpha43

def test_v500_alpha43_c_contract_block(): assert BrokerOrderFacadeV500Alpha43().contract()['execution_allowed'] is False
