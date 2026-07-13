from app.platform_core.ai_decision.integration.scanner_link import AIDecisionScannerLink

def test_v500_alpha33_c_scanner_candidates(): assert AIDecisionScannerLink().candidates()['ready'] is True