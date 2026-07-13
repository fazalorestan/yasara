from app.platform_core.ai_decision.confidence import AIConfidenceEngine

def test_v500_alpha33_a_confidence_weighted(): assert AIConfidenceEngine().calculate([{'score':80,'weight':1},{'score':60,'weight':1}])['confidence']==70
