from app.final_integration_v1.phase1_summary import FinalIntegrationPhase1SummaryBuilderV1

def test_final_integration_phase1_summary():
    summary = FinalIntegrationPhase1SummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.previous_confirmed_tests >= 248
