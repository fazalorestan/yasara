from app.v500_alpha38_exchange_core.models import ExchangeCoreSummaryV500Alpha38

def test_v500_alpha38_a_summary():
 s=ExchangeCoreSummaryV500Alpha38(); assert s.ready and s.test_pack_size==60