from app.v20_final_release.service import V20FinalReleaseService

def test_v2_0_final_release_summary():
    summary = V20FinalReleaseService().summary()
    assert summary["ready"] is True
    assert summary["version"] == "2.0.0"
    assert summary["project_progress_percent"] == 100
    assert summary["remaining_percent"] == 0
