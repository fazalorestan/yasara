from app.v446_indicator_scanner_watchlist.service import IndicatorScannerWatchlistFacadeV446

def test_v446_facade():
    f = IndicatorScannerWatchlistFacadeV446()
    assert f.summary().ready is True
    assert f.contract()["execution_allowed"] is False
    assert f.sample()["count"] == 3
