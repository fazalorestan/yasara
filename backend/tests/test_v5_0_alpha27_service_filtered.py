from app.platform_core.scanner.service import ScannerFoundationService

def test_v500_alpha27_service_filtered(): assert len(ScannerFoundationService().filtered()['accepted']) == 2
