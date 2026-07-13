from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_safety():
 r=BrokerAccountFacadeV500Alpha43().safety(); assert r is not None
