from app.v40_market_context.models import AutoTradeGateRequestV40
from app.v40_market_context.service import MarketContextServiceV40

def test_v40_autotrade_gate_allowed_no_execution():
    data = MarketContextServiceV40().autotrade_gate(AutoTradeGateRequestV40(
        build_type='personal',
        license_key='YASARA-PERSONAL-RASOUL-2026',
        has_exchange_api_key=True,
        checkbox_enabled=True,
        risk_guard_enabled=True,
        kill_switch_active=False
    ))
    assert data["allowed"] is True
    assert data["execution_engine_loaded"] is False
