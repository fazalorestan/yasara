from app.v500_alpha37_broker_enterprise.service import BrokerEnterpriseFacadeV500Alpha37

def test_v500_alpha37_d_facade_quality_score():
 r=BrokerEnterpriseFacadeV500Alpha37().quality_score(); assert r is not None
