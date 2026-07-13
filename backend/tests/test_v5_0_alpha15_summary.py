from app.v500_alpha15_market_data.models import MarketDataSummaryV500Alpha15
def test_v500_alpha15_summary():
    s = MarketDataSummaryV500Alpha15()
    assert s.ready is True
    assert s.test_pack_size == 20
    assert s.real_exchange_connection is False
