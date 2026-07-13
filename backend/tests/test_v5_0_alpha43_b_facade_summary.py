from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_summary():
 r=BrokerAccountFacadeV500Alpha43().summary(); assert r is not None
