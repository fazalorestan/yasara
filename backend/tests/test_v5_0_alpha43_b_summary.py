from app.v500_alpha43_broker_account.models import BrokerAccountSummaryV500Alpha43

def test_v500_alpha43_b_summary():
 s=BrokerAccountSummaryV500Alpha43(); assert s.ready and s.test_pack_size==60
