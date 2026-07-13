from app.final_docs_qa_v1.phase3_summary import FinalDocsQASummaryBuilderV1

def test_phase3_summary():
    summary = FinalDocsQASummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.previous_confirmed_tests >= 263
