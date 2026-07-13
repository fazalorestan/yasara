from app.platform_core.strategy_engine.confidence_model import StrategyConfidenceModel

def test_v500_alpha41_b_confidence(): assert StrategyConfidenceModel().confidence()['confidence_band']=='low'
