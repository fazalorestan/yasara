from app.platform_core.portfolio_intelligence.analytics_readiness import PortfolioAnalyticsRiskReadinessGate

def test_v500_alpha35_b_readiness_block(): assert PortfolioAnalyticsRiskReadinessGate().run()['execution_allowed'] is False
