from app.platform_core.strategy_engine.scoring_safety import StrategyScoringSafetyPolicy

def test_v500_alpha41_b_emit_block(): assert StrategyScoringSafetyPolicy().can_emit_executable_signal()['allowed'] is False
