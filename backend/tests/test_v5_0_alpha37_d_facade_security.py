from app.v500_alpha37_broker_enterprise.service import BrokerEnterpriseFacadeV500Alpha37

def test_v500_alpha37_d_facade_security():
 r=BrokerEnterpriseFacadeV500Alpha37().security(); assert r is not None
