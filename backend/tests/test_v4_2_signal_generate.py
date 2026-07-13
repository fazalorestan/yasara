from app.v42_signal_engine.models import SignalRequestV42
from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42

def test_v42_generate():
    data = MultiLayerSignalEngineServiceV42().generate(SignalRequestV42())
    assert data["ready"] is True
    assert "signal" in data
    assert data["commercial_execution_included"] is False
    assert data["live_trading_enabled"] is False
