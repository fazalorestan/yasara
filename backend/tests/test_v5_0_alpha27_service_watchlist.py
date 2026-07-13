from app.platform_core.scanner.service import ScannerFoundationService

def test_v500_alpha27_service_watchlist(): assert ScannerFoundationService().watchlist()['ready'] is True
