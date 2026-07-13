from app.v500_alpha27_scanner.models import ScannerSummaryV500Alpha27

def test_v500_alpha27_summary():
    s=ScannerSummaryV500Alpha27(); assert s.ready is True; assert s.auto_trading_enabled is False
