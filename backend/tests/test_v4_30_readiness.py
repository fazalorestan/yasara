from app.platform_core.diagnostics.readiness import PlatformReadinessEvaluator

def test_v430_readiness():
    report = PlatformReadinessEvaluator().run()
    assert report.ready is True
    assert report.score >= 80
