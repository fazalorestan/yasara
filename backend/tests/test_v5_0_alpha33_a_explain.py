from app.platform_core.ai_decision.explainability import AIExplainabilityEngine

def test_v500_alpha33_a_explain(): assert AIExplainabilityEngine().explain({'symbol':'BTCUSDT'}, [{'direction':'long'}], 80)['dominant_direction']=='long'
