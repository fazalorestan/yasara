from app.v500_alpha38_exchange_market_data.models import ExchangeMarketDataSummaryV500Alpha38

def test_v500_alpha38_b_summary():
 s=ExchangeMarketDataSummaryV500Alpha38(); assert s.ready and s.test_pack_size==60