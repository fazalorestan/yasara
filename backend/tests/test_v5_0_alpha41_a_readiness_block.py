from app.platform_core.strategy_engine.readiness import StrategyCoreReadinessGate

def test_v500_alpha41_a_readiness_block(): assert StrategyCoreReadinessGate().run()['execution_allowed'] is False
