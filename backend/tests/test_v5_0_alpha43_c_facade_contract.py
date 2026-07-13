from app.v500_alpha43_broker_order.service import BrokerOrderFacadeV500Alpha43

def test_v500_alpha43_c_facade_contract():
 r=BrokerOrderFacadeV500Alpha43().contract(); assert r is not None
