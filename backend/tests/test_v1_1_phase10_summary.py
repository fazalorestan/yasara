from app.v11_backtest_replay.phase10_summary import V11Phase10SummaryBuilder

def test_v11_phase10_summary():
    summary = V11Phase10SummaryBuilder().build()
    assert summary.ready is True
    assert "strategy_backtest_runner" in summary.capabilities
    assert summary.safety == "backtest_and_replay_only_no_live_execution"
