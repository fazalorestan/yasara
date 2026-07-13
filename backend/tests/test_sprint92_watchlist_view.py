from app.desktop_ui_v1.watchlist_view import WatchlistRowV1, WatchlistViewBuilderV1

def test_watchlist_sort_by_change():
    rows = [WatchlistRowV1(symbol="A", exchange="x", price=1, change_percent=1), WatchlistRowV1(symbol="B", exchange="x", price=1, change_percent=5)]
    assert WatchlistViewBuilderV1().sort_by_change(rows)[0].symbol == "B"
