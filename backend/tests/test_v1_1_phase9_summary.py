from app.v11_strategy_runtime.phase9_summary import V11Phase9SummaryBuilder

def test_v11_phase9_summary():
    summary = V11Phase9SummaryBuilder().build()
    assert summary.ready is True
    assert "strategy_rule_engine" in summary.capabilities
    assert summary.safety == "strategy_signal_only_no_live_execution"
