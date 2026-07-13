from app.v415_neowave.models import NeoWaveRequestV415
from app.v415_neowave.service import NeoWaveEngineServiceV415
def test_v415_analyze():
    data=NeoWaveEngineServiceV415().analyze(NeoWaveRequestV415(limit=100))
    assert data["ready"] is True
    assert "neowave" in data
    assert data["real_order_execution_enabled"] is False
