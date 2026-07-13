from app.v500_alpha43_broker_order.models import BrokerOrderSummaryV500Alpha43

def test_v500_alpha43_c_guard(): assert BrokerOrderSummaryV500Alpha43().ready is True
