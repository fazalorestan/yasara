from app.platform_core.scanner.risk_link import ScannerRiskLinkService

def test_v500_alpha27_risk_link_bad(): assert ScannerRiskLinkService().check({'risk_pct':3})['allowed'] is False
