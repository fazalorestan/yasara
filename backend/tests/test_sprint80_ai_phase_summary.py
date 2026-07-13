from app.ai_trading_v1.phase2_summary import AITradingPhaseSummaryBuilderV1

def test_ai_phase_summary_ready():
    summary = AITradingPhaseSummaryBuilderV1().build()
    assert summary.ready is True
    assert "recommendation" in summary.modules
