from app.v36_phase_a_meta_ykb.models import TechnicalDebtItemV36
from app.v36_phase_a_meta_ykb.service import PhaseAMetaYKBServiceV36

def test_v36_add_tech_debt():
    service = PhaseAMetaYKBServiceV36()
    item = service.add_technical_debt(TechnicalDebtItemV36(id="TD-TEST-V36", description="test debt"))
    assert item["ready"] is True
