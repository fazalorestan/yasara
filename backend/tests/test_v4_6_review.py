from app.v46_trading_journal.models import JournalEntryV46
from app.v46_trading_journal.service import TradingJournalServiceV46

def test_v46_review():
    s = TradingJournalServiceV46()
    s.add_entry(JournalEntryV46(id="test-review-v46", pnl=-5, quantity=1, emotion="fear"))
    data = s.review("test-review-v46")
    assert data["ready"] is True
    assert "discipline_score" in data
    assert data["real_order_execution_enabled"] is False
