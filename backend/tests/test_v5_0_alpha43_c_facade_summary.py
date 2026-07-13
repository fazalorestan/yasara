from app.v500_alpha43_broker_order.service import BrokerOrderFacadeV500Alpha43

def test_v500_alpha43_c_facade_summary():
 r=BrokerOrderFacadeV500Alpha43().summary(); assert r is not None
