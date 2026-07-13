from app.v500_alpha6_indicator_math.models import IndicatorMathSummaryV500Alpha6

def test_v500_alpha6_summary():
    s = IndicatorMathSummaryV500Alpha6()
    assert s.ready is True
    assert s.live_execution_enabled is False
