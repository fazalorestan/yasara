from app.v21_real_data.service import RealDataActivationServiceV21
from app.v21_real_data.models import WatchlistItemV21

def test_real_data_watchlist_add_remove():
    service = RealDataActivationServiceV21()
    service.add_watchlist_item(WatchlistItemV21(symbol="TESTUSDT", exchange="binance"))
    assert any(x.symbol == "TESTUSDT" for x in service.get_watchlist().items)
    service.remove_watchlist_item("TESTUSDT", "binance")
