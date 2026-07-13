from app.platform_core.scanner.service import ScannerFoundationService

def test_v500_alpha27_service_ranked(): assert ScannerFoundationService().ranked()['items'][0]['score'] >= 65
