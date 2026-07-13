from app.v500_alpha37_broker_orders_account.service import BrokerOrdersAccountFacadeV500Alpha37

def test_v500_alpha37_b_facade_summary():
 r=BrokerOrdersAccountFacadeV500Alpha37().summary(); assert r is not None
