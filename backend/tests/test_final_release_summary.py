from app.final_release_v1.final_release_summary import FinalReleaseSummaryBuilderV1

def test_final_release_summary():
    summary = FinalReleaseSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.version == "1.0.0"
