from app.v49_market_structure.models import MarketStructureRequestV49
from app.v49_market_structure.service import ProfessionalMarketStructureServiceV49

def test_v49_analyze():
    data = ProfessionalMarketStructureServiceV49().analyze(MarketStructureRequestV49(limit=100))
    assert data["ready"] is True
    assert "structure" in data
    assert data["real_order_execution_enabled"] is False
