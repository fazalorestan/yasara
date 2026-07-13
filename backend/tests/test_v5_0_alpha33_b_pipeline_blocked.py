from app.platform_core.ai_decision.pipeline import AIDecisionPipeline

def test_v500_alpha33_b_pipeline_blocked(): assert AIDecisionPipeline().run({'symbol':'BTCUSDT'}, [])['execution_allowed'] is False
