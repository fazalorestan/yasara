from app.v441_yasara_indicator.service import YaSaraIndicatorServiceV441

def test_v441_service():
    s = YaSaraIndicatorServiceV441()
    assert s.summary().ready is True
    assert s.registry()["ready"] is True
    assert s.default_state()["enabled"] is True
