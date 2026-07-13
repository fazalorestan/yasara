from app.v500_alpha37_broker_enterprise.service import BrokerEnterpriseFacadeV500Alpha37

def test_v500_alpha37_d_contract_block(): assert BrokerEnterpriseFacadeV500Alpha37().contract()['execution_allowed'] is False
