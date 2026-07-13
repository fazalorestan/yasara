from app.v500_alpha37_broker_core.service import BrokerCoreFacadeV500Alpha37

def test_v500_alpha37_a_facade_contract():
 r=BrokerCoreFacadeV500Alpha37().contract(); assert r is not None
