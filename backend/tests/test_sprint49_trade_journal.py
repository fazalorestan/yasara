from app.productivity_v1.trade_journal import TradeJournalBookV1, TradeJournalRecordV1

def test_trade_journal_total_pnl():
    book = TradeJournalBookV1()
    book.add(TradeJournalRecordV1(trade_id="t1", symbol="BTC/USDT", direction="long", pnl=5))
    book.add(TradeJournalRecordV1(trade_id="t2", symbol="BTC/USDT", direction="short", pnl=-2))
    assert book.total_pnl() == 3
    assert len(book.list("BTC/USDT")) == 2
