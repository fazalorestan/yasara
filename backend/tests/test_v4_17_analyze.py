from app.v417_elliott.models import ElliottRequestV417
from app.v417_elliott.service import ElliottEngineServiceV417
def test_v417_analyze():
    data=ElliottEngineServiceV417().analyze(ElliottRequestV417(limit=100))
    assert data["ready"] is True
    assert "elliott" in data
    assert data["real_order_execution_enabled"] is False
