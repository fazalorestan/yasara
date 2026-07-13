from app.v500_alpha43_broker_core.service import BrokerCoreFacadeV500Alpha43

def test_v500_alpha43_a_facade_safety():
 r=BrokerCoreFacadeV500Alpha43().safety(); assert r is not None
