from app.platform_core.ai_decision.confidence import AIConfidenceEngine

def test_v500_alpha33_a_confidence_empty(): assert AIConfidenceEngine().calculate([])['confidence']==0.0
