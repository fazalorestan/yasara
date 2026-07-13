from app.platform_core.ai_decision.integration.scanner_link import AIDecisionScannerLink

def test_v500_alpha33_c_scanner_evidence(): assert isinstance(AIDecisionScannerLink().evidence()['evidence'], list)