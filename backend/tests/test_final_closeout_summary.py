from app.final_closeout_v1.closeout_summary import FinalCloseoutSummaryBuilderV1

def test_closeout_summary():
    summary = FinalCloseoutSummaryBuilderV1().build()
    assert summary.project_complete is True
    assert summary.confirmed_tests >= 285
