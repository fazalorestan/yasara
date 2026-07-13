from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_readiness():
 r=BrokerAccountFacadeV500Alpha43().readiness(); assert r is not None
