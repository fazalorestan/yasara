from app.v42_signal_engine.models import SignalRequestV42
from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42

def test_v42_commercial_blocks_execution():
    data = MultiLayerSignalEngineServiceV42().generate(SignalRequestV42(build_type='commercial', autotrade_checkbox_enabled=True))
    assert data["signal"]["execution_allowed"] is False
    assert data["commercial_execution_included"] is False
