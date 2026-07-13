from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_facade_report():
 r=BrokerAccountFacadeV500Alpha43().report(); assert r is not None
