from app.platform_core.scanner.service import ScannerFoundationService

def test_v500_alpha27_service_scan():
    r=ScannerFoundationService().scan(); assert r['ready'] is True; assert r['execution_allowed'] is False
