from app.productivity_v1.portfolio_analytics import PortfolioAnalyticsEngineV1, PortfolioAnalyticsInputV1

def test_portfolio_analytics_profit():
    result = PortfolioAnalyticsEngineV1().analyze(
        PortfolioAnalyticsInputV1(equity=11000, initial_equity=10000, realized_pnl=700, unrealized_pnl=300)
    )
    assert result.total_pnl == 1000
    assert result.status == "profit"
