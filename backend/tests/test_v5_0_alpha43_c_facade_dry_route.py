from app.v500_alpha43_broker_order.service import BrokerOrderFacadeV500Alpha43

def test_v500_alpha43_c_facade_dry_route():
 r=BrokerOrderFacadeV500Alpha43().dry_route(); assert r is not None
