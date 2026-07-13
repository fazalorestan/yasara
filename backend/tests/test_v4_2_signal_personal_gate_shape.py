from app.v42_signal_engine.models import SignalRequestV42
from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42

def test_v42_personal_gate_shape():
    data = MultiLayerSignalEngineServiceV42().generate(SignalRequestV42(
        build_type='personal',
        license_key='YASARA-PERSONAL-RASOUL-2026',
        has_exchange_api_key=True,
        autotrade_checkbox_enabled=True
    ))
    assert "autotrade_gate" in data
    assert data["signal"]["real_order_execution_enabled"] is False
