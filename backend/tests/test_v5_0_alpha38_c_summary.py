from app.v500_alpha38_exchange_connectivity.models import ExchangeConnectivitySummaryV500Alpha38

def test_v500_alpha38_c_summary():
 s=ExchangeConnectivitySummaryV500Alpha38(); assert s.ready and s.test_pack_size==60