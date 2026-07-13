from app.v11_backtest_replay.service import BacktestReplayServiceV11

def test_backtest_replay_service_summary_payload():
    payload = BacktestReplayServiceV11().summary_payload()
    assert payload["ready"] is True
    assert payload["safety"] == "backtest_only_no_live_execution"
