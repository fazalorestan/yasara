from app.v52_enterprise_trading_os.service import EnterpriseTradingOSService

def test_service_snapshot():
    s = EnterpriseTradingOSService().snapshot()
    assert s.build_id == "2026.43.ENTERPRISE.001"
    assert [w.workspace for w in s.workspaces] == ["trader", "ai", "portfolio", "developer"]
