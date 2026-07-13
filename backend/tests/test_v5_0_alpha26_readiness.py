from app.platform_core.portfolio_manager.readiness import PortfolioManagerReadinessGate

def test_v500_alpha26_readiness():
    r=PortfolioManagerReadinessGate().run(); assert r['ready'] is True; assert r['execution_allowed'] is False
