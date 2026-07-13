from app.platform_core.strategy_engine.capital_allocation import StrategyCapitalAllocationContract

def test_v500_alpha41_c_capital(): assert StrategyCapitalAllocationContract().capital_plan()['deployable_capital']==0.0
