from app.cloud_v1.phase4_summary import CloudPhaseSummaryBuilderV1

def test_cloud_phase_summary():
    summary = CloudPhaseSummaryBuilderV1().build()
    assert summary.ready is True
    assert "license" in summary.modules
