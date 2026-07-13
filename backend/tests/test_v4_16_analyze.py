from app.v416_neowave_sprint2.models import NeoWaveSprint2RequestV416
from app.v416_neowave_sprint2.service import NeoWaveSprint2ServiceV416
def test_v416_analyze():
    data=NeoWaveSprint2ServiceV416().analyze(NeoWaveSprint2RequestV416(limit=100))
    assert data["ready"] is True
    assert "neowave_sprint2" in data
    assert data["real_order_execution_enabled"] is False
