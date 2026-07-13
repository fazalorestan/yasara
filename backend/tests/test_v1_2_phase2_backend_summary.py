from app.v12_market_workspace.service import MarketWorkspaceServiceV12
def test_market_workspace_summary():
    summary = MarketWorkspaceServiceV12().summary()
    assert summary["ready"] is True
    assert summary["progress_percent"] == 50
    assert "watchlist" in summary["capabilities"]
