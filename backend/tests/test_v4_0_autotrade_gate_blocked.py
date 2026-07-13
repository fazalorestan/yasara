from app.v40_market_context.models import AutoTradeGateRequestV40
from app.v40_market_context.service import MarketContextServiceV40

def test_v40_autotrade_gate_blocked():
    data = MarketContextServiceV40().autotrade_gate(AutoTradeGateRequestV40(build_type='commercial', checkbox_enabled=True))
    assert data["allowed"] is False
    assert data["commercial_included"] is False
    assert data["real_order_execution_enabled"] is False
