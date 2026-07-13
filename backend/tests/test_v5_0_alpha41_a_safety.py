from app.platform_core.strategy_engine.safety import StrategySafetyPolicy

def test_v500_alpha41_a_safety(): assert StrategySafetyPolicy().policy()['advisory_only'] is True
