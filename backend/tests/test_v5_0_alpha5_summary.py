from app.v500_alpha5_indicator_release_gate.models import IndicatorReleaseGateSummaryV500Alpha5

def test_v500_alpha5_summary():
    s = IndicatorReleaseGateSummaryV500Alpha5()
    assert s.ready is True
    assert s.milestone == "1000_tests"
    assert s.live_execution_enabled is False
