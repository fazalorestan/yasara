from app.v446_indicator_scanner_watchlist.models import IndicatorScannerWatchlistSummaryV446

def test_v446_summary():
    s = IndicatorScannerWatchlistSummaryV446()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
