from app.platform_core.strategy_engine.enterprise.service import StrategyEnterpriseService

def test_v500_alpha41_e_service_performance():
 r=StrategyEnterpriseService().performance(); assert r is not None
