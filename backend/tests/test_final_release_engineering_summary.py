from app.final_release_engineering_v1.release_engineering_summary import ReleaseEngineeringSummaryBuilderV1

def test_release_engineering_summary():
    summary = ReleaseEngineeringSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.previous_confirmed_tests >= 256
