from app.dashboard_v1.engine.watchlist import DashboardWatchlistEngineV1

def test_watchlist_enrich_prices():
    items = DashboardWatchlistEngineV1().enrich({"BTC/USDT": 60000}, {"BTC/USDT": 77})
    assert items[0].symbol == "BTC/USDT"
    assert items[0].price == 60000
    assert items[0].confidence == 77
