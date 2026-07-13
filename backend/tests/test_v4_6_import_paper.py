from app.v46_trading_journal.service import TradingJournalServiceV46

def test_v46_import_paper():
    data = TradingJournalServiceV46().import_paper_orders()
    assert data["ready"] is True
    assert "imported_count" in data
