from app.v444_indicator_pine_source.service import IndicatorPineSourceServiceV444

def test_v444_service():
    s = IndicatorPineSourceServiceV444()
    assert s.summary().ready is True
    assert s.archive()["ready"] is True
    assert s.source_status()["execution_allowed"] is False
