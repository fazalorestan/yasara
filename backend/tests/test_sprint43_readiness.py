from app.platform_core.trading_os_enterprise.readiness import TradingOSEnterpriseReadinessGate

def test_readiness():
    assert TradingOSEnterpriseReadinessGate().run()["ready"] is True
