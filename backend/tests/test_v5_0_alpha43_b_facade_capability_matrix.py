from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_capability_matrix():
 r=BrokerAccountFacadeV500Alpha43().capability_matrix(); assert r is not None
