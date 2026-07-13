from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_contract():
 r=BrokerAccountFacadeV500Alpha43().contract(); assert r is not None
