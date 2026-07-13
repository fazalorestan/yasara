from app.v500_alpha43_broker_core.service import BrokerCoreFacadeV500Alpha43

def test_v500_alpha43_a_facade_readiness():
 r=BrokerCoreFacadeV500Alpha43().readiness(); assert r is not None
