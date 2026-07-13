from app.productivity_v1.favorites import FavoriteSymbolBookV1, FavoriteSymbolServiceV1

def test_favorite_symbols_add_remove():
    service = FavoriteSymbolServiceV1()
    book = service.add(FavoriteSymbolBookV1(), "btc/usdt")
    assert "BTC/USDT" in book.symbols
    book = service.remove(book, "BTC/USDT")
    assert book.symbols == []
