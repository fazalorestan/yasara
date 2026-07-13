from app.v46_trading_journal.service import TradingJournalServiceV46

def test_v46_summary():
    s = TradingJournalServiceV46().summary()
    assert s.product_progress_percent == 97
    assert s.constitution_compliant is True
