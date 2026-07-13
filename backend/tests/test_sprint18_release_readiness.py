from app.release_v1.engine.readiness import ReleaseReadinessEngineV1

def test_release_readiness_passes_required_checks():
    report = ReleaseReadinessEngineV1().run()
    assert report.ready is True
    assert any(c.key == "docker" for c in report.checks)
