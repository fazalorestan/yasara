from app.v431_release_readiness.service import ReleaseReadinessServiceV431

def test_v431_service():
    s = ReleaseReadinessServiceV431()
    assert s.summary().ready is True
    assert s.gate()["ready"] is True
    assert s.security()["ready"] is True
