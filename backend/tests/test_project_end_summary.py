from app.project_end_v1.final_end_summary import FinalEndSummaryBuilderV1

def test_project_end_summary():
    summary = FinalEndSummaryBuilderV1().build()
    assert summary.complete is True
    assert summary.next_action == "create_final_zip_archive"
