from app.v500_alpha37_broker_core.service import BrokerCoreFacadeV500Alpha37

def test_v500_alpha37_a_facade_default_broker():
 r=BrokerCoreFacadeV500Alpha37().default_broker(); assert r is not None
