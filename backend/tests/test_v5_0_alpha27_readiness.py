from app.platform_core.scanner.readiness import ScannerReadinessGate

def test_v500_alpha27_readiness():
    r=ScannerReadinessGate().run(); assert r['ready'] is True; assert r['execution_allowed'] is False
