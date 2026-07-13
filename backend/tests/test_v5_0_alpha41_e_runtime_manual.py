from app.platform_core.strategy_engine.enterprise.runtime_acceptance import StrategyEnterpriseRuntimeAcceptance

def test_v500_alpha41_e_runtime_manual(): assert StrategyEnterpriseRuntimeAcceptance().contract()['manual_apply_required'] is False
