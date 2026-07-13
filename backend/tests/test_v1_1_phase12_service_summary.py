from app.v11_final_release.service import FinalReleaseServiceV11

def test_final_release_service_summary():
    summary = FinalReleaseServiceV11().summary()
    assert summary.ready is True
    assert summary.progress_percent == 100
    assert summary.checks_passed == summary.checks_total
