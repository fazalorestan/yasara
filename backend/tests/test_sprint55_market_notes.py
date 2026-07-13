from app.productivity_v1.market_notes import MarketNoteV1, MarketNotesBookV1

def test_market_notes_by_symbol():
    book = MarketNotesBookV1()
    book.add(MarketNoteV1(note_id="n1", symbol="BTC/USDT", text="breakout"))
    assert book.list("BTC/USDT")[0].text == "breakout"
