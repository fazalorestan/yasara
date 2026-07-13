from app.platform_core.ai_decision.confidence import AIConfidenceEngine

def test_v500_alpha33_a_confidence_invalid(): assert AIConfidenceEngine().calculate([{'score':80,'weight':0}])['ready'] is False
