from app.ai_trading_v1.portfolio_optimizer import PortfolioAssetInputV1, PortfolioOptimizerV1

def test_portfolio_optimizer_weights_sum_to_one():
    weights = PortfolioOptimizerV1().optimize([
        PortfolioAssetInputV1(symbol="BTC", expected_return=10, risk_score=5),
        PortfolioAssetInputV1(symbol="ETH", expected_return=5, risk_score=5),
    ])
    assert round(sum(w.weight for w in weights), 6) == 1
