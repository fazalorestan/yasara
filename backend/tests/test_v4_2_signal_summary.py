from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42

def test_v42_summary():
    s = MultiLayerSignalEngineServiceV42().summary()
    assert s.product_progress_percent == 90
    assert s.constitution_compliant is True
