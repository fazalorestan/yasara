from app.v46_trading_journal.models import JournalEntryV46
from app.v46_trading_journal.service import TradingJournalServiceV46

def test_v46_add_entry():
    s = TradingJournalServiceV46()
    data = s.add_entry(JournalEntryV46(id="test-entry-v46", pnl=10, quantity=1))
    assert data["ready"] is True
    assert data["entry"]["id"] == "test-entry-v46"
