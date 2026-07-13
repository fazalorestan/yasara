from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_account_contract():
 r=BrokerAccountFacadeV500Alpha43().account_contract(); assert r is not None
