from app.archive_handoff_v1.project_done_summary import ProjectDoneSummaryBuilderV1

def test_project_done_summary():
    summary = ProjectDoneSummaryBuilderV1().build()
    assert summary.done is True
    assert summary.version == "1.0.0"
