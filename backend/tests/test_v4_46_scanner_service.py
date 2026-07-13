from app.platform_core.indicators.scanner.service import IndicatorScannerContractService

def test_v446_scanner_service():
    result = IndicatorScannerContractService().build([{"scanner": {"symbol": "A", "direction": "LONG", "score": 70}}])
    assert result["ready"] is True
    assert result["count"] == 1
