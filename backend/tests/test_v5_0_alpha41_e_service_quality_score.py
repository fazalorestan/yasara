from app.platform_core.strategy_engine.enterprise.service import StrategyEnterpriseService

def test_v500_alpha41_e_service_quality_score():
 r=StrategyEnterpriseService().quality_score(); assert r is not None
