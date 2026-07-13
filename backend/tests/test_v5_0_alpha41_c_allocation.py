from app.platform_core.strategy_engine.portfolio_allocation import StrategyPortfolioAllocationEngine

def test_v500_alpha41_c_allocation(): assert StrategyPortfolioAllocationEngine().allocation()['mode']=='advisory_only'
