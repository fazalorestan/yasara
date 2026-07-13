from app.v421_market_structure_pro.models import MarketStructureProRequestV421
from app.v421_market_structure_pro.service import MarketStructureProServiceV421

def test_v421_analyze():
    data = MarketStructureProServiceV421().analyze(MarketStructureProRequestV421(limit=120))
    assert data["ready"] is True
    assert "market_structure_pro" in data
    assert data["real_order_execution_enabled"] is False
