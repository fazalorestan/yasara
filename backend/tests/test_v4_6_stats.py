from app.v46_trading_journal.service import TradingJournalServiceV46

def test_v46_stats():
    data = TradingJournalServiceV46().stats()
    assert data["ready"] is True
    assert "win_rate" in data
