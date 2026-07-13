from app.platform_core.scanner.watchlist import ScannerWatchlistService

def test_v500_alpha27_watchlist(): assert 'BTCUSDT' in ScannerWatchlistService().default_watchlist()['symbols']
