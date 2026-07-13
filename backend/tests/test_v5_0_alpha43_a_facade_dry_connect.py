from app.v500_alpha43_broker_core.service import BrokerCoreFacadeV500Alpha43

def test_v500_alpha43_a_facade_dry_connect():
 r=BrokerCoreFacadeV500Alpha43().dry_connect(); assert r is not None
