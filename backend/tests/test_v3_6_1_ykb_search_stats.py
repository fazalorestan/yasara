from app.v361_phase_a_guardrails.models import YKBSearchRequestV361
from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

def test_v361_ykb_search_stats():
    service = PhaseAGuardrailsServiceV361()
    search = service.ykb_search(YKBSearchRequestV361(query='YKB'))
    stats = service.ykb_stats()
    assert search["ready"] is True
    assert stats["ready"] is True
