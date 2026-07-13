from app.platform_core.portfolio_intelligence.analytics_service import PortfolioAnalyticsRiskService

def test_v500_alpha35_b_risk_grade_valid(): assert PortfolioAnalyticsRiskService().risk_score()['risk_grade'] in ['low','medium','high']
