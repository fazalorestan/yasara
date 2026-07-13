from app.v420_trading_workspace.models import TradingWorkspaceSummaryV420

def test_v420_trading_workspace_backend():
    s = TradingWorkspaceSummaryV420()
    assert s.ready is True
    assert s.constitution_compliant is True
