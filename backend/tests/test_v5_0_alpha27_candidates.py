from app.platform_core.scanner.candidates import ScannerCandidateProvider

def test_v500_alpha27_candidates(): assert len(ScannerCandidateProvider().sample_candidates()) == 4
