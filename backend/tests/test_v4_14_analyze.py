from app.v414_ai_fusion.models import AIDecisionFusionRequestV414
from app.v414_ai_fusion.service import AIDecisionFusionServiceV414
def test_v414_analyze():
    data=AIDecisionFusionServiceV414().analyze(AIDecisionFusionRequestV414(limit=100))
    assert data["ready"] is True
    assert "decision" in data
    assert data["real_order_execution_enabled"] is False
