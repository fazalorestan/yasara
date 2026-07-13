from app.v441_yasara_indicator.models import YaSaraIndicatorSummaryV441

def test_v441_summary():
    s = YaSaraIndicatorSummaryV441()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.enabled_by_default is True
    assert s.live_execution_enabled is False
