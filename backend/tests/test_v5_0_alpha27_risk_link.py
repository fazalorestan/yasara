from app.platform_core.scanner.risk_link import ScannerRiskLinkService

def test_v500_alpha27_risk_link(): assert ScannerRiskLinkService().check({'risk_pct':1})['allowed'] is True
