from app.platform_core.strategy_engine.readiness import StrategyCoreReadinessGate

def test_v500_alpha41_a_readiness(): assert StrategyCoreReadinessGate().run()['ready'] is True
