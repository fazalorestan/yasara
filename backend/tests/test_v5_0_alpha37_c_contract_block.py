from app.v500_alpha37_broker_connectivity.service import BrokerConnectivityFacadeV500Alpha37

def test_v500_alpha37_c_contract_block(): assert BrokerConnectivityFacadeV500Alpha37().contract()['execution_allowed'] is False
