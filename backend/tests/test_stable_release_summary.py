from app.stable_release_v1.stable_summary import StableReleaseSummaryBuilderV1

def test_stable_summary():
    summary = StableReleaseSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.version == "1.0.0"
