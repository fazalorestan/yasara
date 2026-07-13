from app.v500_alpha37_broker_orders_account.service import BrokerOrdersAccountFacadeV500Alpha37

def test_v500_alpha37_b_contract_block(): assert BrokerOrdersAccountFacadeV500Alpha37().contract()['execution_allowed'] is False
