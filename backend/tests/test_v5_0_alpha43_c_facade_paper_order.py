from app.v500_alpha43_broker_order.service import BrokerOrderFacadeV500Alpha43

def test_v500_alpha43_c_facade_paper_order():
 r=BrokerOrderFacadeV500Alpha43().paper_order(); assert r is not None
