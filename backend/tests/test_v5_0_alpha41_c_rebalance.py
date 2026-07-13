from app.platform_core.strategy_engine.portfolio_balancer import StrategyPortfolioBalancer

def test_v500_alpha41_c_rebalance(): assert StrategyPortfolioBalancer().rebalance_plan()['executed'] is False
