from app.platform_core.strategy_engine.safety import StrategySafetyPolicy

def test_v500_alpha41_a_can_execute(): assert StrategySafetyPolicy().can_execute()['allowed'] is False
