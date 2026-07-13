from app.v413_ict_engine.models import ICTEngineRequestV413
from app.v413_ict_engine.service import ICTEngineServiceV413
def test_v413_analyze():
    data=ICTEngineServiceV413().analyze(ICTEngineRequestV413(limit=100))
    assert data["ready"] is True
    assert "ict" in data
    assert data["real_order_execution_enabled"] is False
