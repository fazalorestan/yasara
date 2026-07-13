from app.platform_core.strategy_engine.position_sizing import StrategyPositionSizingContract

def test_v500_alpha41_c_position(): assert StrategyPositionSizingContract().size()['position_size']==0.0
