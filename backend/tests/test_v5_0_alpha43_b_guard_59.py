from app.v500_alpha43_broker_account.models import BrokerAccountSummaryV500Alpha43

def test_v500_alpha43_b_guard(): assert BrokerAccountSummaryV500Alpha43().ready is True
