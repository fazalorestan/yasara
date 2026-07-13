from app.v500_alpha37_broker_orders_account.models import BrokerOrdersAccountSummaryV500Alpha37

def test_v500_alpha37_b_summary():
 s=BrokerOrdersAccountSummaryV500Alpha37(); assert s.ready and s.test_pack_size==60