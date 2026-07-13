from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_dry_account():
 r=BrokerAccountFacadeV500Alpha43().dry_account(); assert r is not None
