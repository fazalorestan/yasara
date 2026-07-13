from app.platform_core.strategy_engine.enterprise.readiness import StrategyEnterpriseReadinessGate

def test_v500_alpha41_e_readiness_block(): assert StrategyEnterpriseReadinessGate().run()['execution_allowed'] is False
