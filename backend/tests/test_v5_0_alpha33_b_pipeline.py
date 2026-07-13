from app.platform_core.ai_decision.pipeline import AIDecisionPipeline

def test_v500_alpha33_b_pipeline():
 r=AIDecisionPipeline().run({'symbol':'BTCUSDT'}, [{'direction':'long','score':80,'weight':1}]); assert r['ready'] is True
