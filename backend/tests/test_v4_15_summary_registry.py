from app.v415_neowave.service import NeoWaveEngineServiceV415
from app.v415_engine_registry_pro.registry import EngineRegistryProV415
def test_v415_summary_registry():
    assert NeoWaveEngineServiceV415().summary().ready is True
    r=EngineRegistryProV415().list()
    assert r["ready"] is True
    assert "neowave" in r["engines"]
