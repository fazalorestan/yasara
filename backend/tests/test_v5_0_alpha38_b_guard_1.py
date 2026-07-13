from app.v500_alpha38_exchange_market_data.models import ExchangeMarketDataSummaryV500Alpha38

def test_v500_alpha38_b_guard(): assert ExchangeMarketDataSummaryV500Alpha38().ready is True
