from app.v36_phase_a_meta_ykb.models import YKBEntryV36
from app.v36_phase_a_meta_ykb.service import PhaseAMetaYKBServiceV36

def test_v36_ykb_add_entry():
    service = PhaseAMetaYKBServiceV36()
    result = service.add_ykb(YKBEntryV36(id="test-v36-entry", title="Test", content="Test content"))
    assert result["ready"] is True
    assert result["entry"]["id"] == "test-v36-entry"
