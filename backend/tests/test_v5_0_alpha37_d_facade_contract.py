from app.v500_alpha37_broker_enterprise.service import BrokerEnterpriseFacadeV500Alpha37

def test_v500_alpha37_d_facade_contract():
 r=BrokerEnterpriseFacadeV500Alpha37().contract(); assert r is not None
