from app.v500_alpha43_broker_core.service import BrokerCoreFacadeV500Alpha43

def test_v500_alpha43_a_facade_contract():
 r=BrokerCoreFacadeV500Alpha43().contract(); assert r is not None
