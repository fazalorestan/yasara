from app.ai_trading_v1.recommendation import AIRecommendationEngineV1, AIRecommendationInputV1

def test_ai_recommendation_wait_on_risk_reject():
    result = AIRecommendationEngineV1().recommend(AIRecommendationInputV1(direction="long", confidence=90, risk_approved=False))
    assert result.action == "wait"
