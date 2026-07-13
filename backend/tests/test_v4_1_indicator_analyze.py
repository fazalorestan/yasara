from app.v41_indicator_engine.models import IndicatorRequestV41
from app.v41_indicator_engine.service import ModularIndicatorEngineServiceV41

def test_v41_analyze():
    data = ModularIndicatorEngineServiceV41().analyze(IndicatorRequestV41(limit=80))
    assert data["ready"] is True
    assert len(data["results"]) >= 10
    assert data["live_trading_enabled"] is False
